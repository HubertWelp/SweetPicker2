# -*- coding: utf-8 -*-
"""
    Klasse für die Dialogführung mit einem Nutzer
    Die Klasse stellt Dialoge für die Begrüßung des Nutzers inklusive der Auswahl eine zu überreichenenden Objektes sowie zur Verabschiedung zur Verfügung
    Die Klasse setzt einen lokalen Broker voraus. Dies kann der "main-broker" auf dem NAO sein oder ein lokaler Stellvertreter-Broker,
    der mit dem NAO verbunden ist.
    Von der Klasse muss ein globales Objekt erzeugt werden. Der Objektname muss dem Konstruktor als Parameter übergeben werden. 
    Beispiel: nd = Nutzerdialog("nd")
    In der Klasse werden Events behandelt. Die Klasse setzt voraus, dass das verwendende Progamm sich einer Endlosschleife befindet.
    Die Dialoge werden in einer iqChat-Topic-Datei (*.top) beschrieben. Diese müssen in jedem Fall auf dem NAO installiert werden, auch wenn das eigentliche Programm
    auf einem externen Rechner ausgeführt wird.
    
    
"""
from naoqi import ALProxy
from naoqi import ALModule
import time
memory = None

class NutzerDialog(ALModule):
    def __init__(self,name):
        ALModule.__init__(self, name)
        self.globalObjectName = name
        self.dialog_p = ALProxy('ALDialog')
        self.tts = ALProxy('ALTextToSpeech')
        self.dialog_p.setLanguage("German")
        # Load topic - absolute path is required
#        self.topf_pathBegruesse = "C:\\Users\\ITL.NAO.1\\Documents\\SWT-SP2\\SweetPicker2\\begruessung_ged.top"
#        self.topf_pathBegruesse = self.topf_pathBegruesse.decode('utf-8')
#        self.topic = self.dialog_p.loadTopic(self.topf_pathBegruesse.encode('utf-8'))
        self.topf_pathBegruesse = "/home/nao/begruessung_ged.top"
        self.topf_pathUeberreiche = "/home/nao/uebereiche_ged.top"
#        self.topf_pathBegruesse = "/home/welp/python/SweetPicker2/begruessung_ged.top"
#        self.topf_pathUeberreiche = "/home/welp/python/SweetPicker2/uebereiche_ged.top"
        global memory
        memory = ALProxy("ALMemory")
        print(self.globalObjectName)
        memory.subscribeToEvent("retDialog",self.globalObjectName,"onReturnDialog")
        self.ret = 0
        
    def begruesse(self):
        """Dialog zur Begruessung des Nutzers und Auswahl des zu überreichenden Objekts.

        Nachdem der NAO den Bentutzer begrüßt hat, erwartet er eine Antwort auf die Begrüßung. Im Anschluss erfolgt ein Dialog, in dem dem Nutzer
        zwei verschiedene Objekte zur Auswahl angeboten werden. Antwortet der Nutzer unverständlich oder nicht ein einem definietem Zeitfenster, wird dies
        als entsprechend zweifacher Ablehnung der angebotenen Objekte als "keine Antwort" interpretiert. 

        Parameters
        ----------
        keine

        Returns
        -------
            0 = keine Antwort bzw. Auswahl
            1 = Objekt 1 (Milky Way)
            2 = Objekt 2 (Mars

        """
        self.ret = -1
        # Start dialog
        self.topic = self.dialog_p.loadTopic(self.topf_pathBegruesse)
        self.dialog_p.subscribe('myModule')

        # Robot starts conservation
        self.tts.say("Guten Tag")
        # Activate dialog
        self.dialog_p.activateTopic(self.topic)

        # Wait for dialog finished
        dialogDauer = 60.0
        dialogStart = time.time()
        while self.ret == -1 and time.time()-dialogStart<dialogDauer:
            time.sleep(1)
        #raw_input(u"Press 'Enter' to exit.")

        # Deactivate topic
        self.dialog_p.deactivateTopic(self.topic)

        # Unload topic
        self.dialog_p.unloadTopic(self.topic)

        # Stop dialog
        self.dialog_p.unsubscribe('myModule')        
        
        return self.ret

    def ueberreiche(self):
        """Dialog zum Anreichen des aufgegriffenen Ojbektes.

        Der Dialog endet spätestens nach 30 Sekunden, auch wenn der Nutzer sich nicht bedankt hat.
        
        Parameters
        ----------
        keine

        Returns
        -------
        keine
        """
        # Start dialog
        self.ret = 0
        self.topic = self.dialog_p.loadTopic(self.topf_pathUeberreiche)
        self.dialog_p.subscribe('myModule')

        # Robot starts conservation
        self.tts.say("Bitte schön")
        # Activate dialog
        self.dialog_p.activateTopic(self.topic)

        # Wait for dialog finished
        dialogDauer = 30.0
        dialogStart = time.time()
        while self.ret==0 and time.time()-dialogStart<dialogDauer:
            time.sleep(1)
        #raw_input(u"Press 'Enter' to exit.")

        # Deactivate topic
        self.dialog_p.deactivateTopic(self.topic)

        # Unload topic
        self.dialog_p.unloadTopic(self.topic)

        # Stop dialog
        self.dialog_p.unsubscribe('myModule')          

    def onReturnDialog(self, *_args):
        """ this method has to be bound because it is a callback. Therefore this comment. """
        r = memory.getData("retDialog")
        self.ret = int(r)
        print(self.ret)
        print("onReturnDialog")
