# -*- coding: utf-8 -*-
"""
    Klasse zur Gesichtserkennung
    Die Klasse setzt einen lokalen Broker voraus. Dies kann der "main-broker" auf dem NAO sein oder ein lokaler Stellvertreter-Broker,
    der mit dem NAO verbunden ist.
    Von der Klasse muss ein globales Objekt erzeugt werden. Der Objektname muss dem Konstruktor als Parameter übergeben werden. 
    Beispiel: ge = Gesichtserkenner("ge")
    Zur Gesichtserkennung muss das anwendende in eine Endlosschleife versetzt werden. Bei Detektion eines Gesichts 
    benachrichtigt das Gesichtserkenner-Objekt einen anderen Programmteil durch Aufruf einer Callback-Funktion, die vorab beim 
    Gesichtserkenner mit der Methode anmelden() registriert werden muss.
"""

from naoqi import ALModule
from naoqi import ALProxy


memory = None

class Gesichtserkenner(ALModule):
		
	def	__init__(self, name):
	    ALModule.__init__(self, name)
	    self.callBack = None
	    self.globalObjectName = name
	    global memory
	    memory = ALProxy("ALMemory")
            memory.subscribeToEvent("FaceDetected",self.globalObjectName,"onFaceDetected")	

		
	def anmelden(self,callBack):
		"""Registrieren zur Benachrichtigung bei einem PersonenErkannt- Ereignis.

                Hiermit meldet sich ein Subscriber-Objekt an, um informiert zu werden, falls von 
		einem Objekt dieser Klasse eine Person erkannt worden ist. Hier zu ist eine Rückrüf (Call-Back)-
		Funktion anzugeben.

                Parameters
                ----------
                callback: Pointer auf Funktion
                        Die Funktion, die aufgerufen werden soll, falls eine PersonenErkannt-Ereignis stattgefunden hat. Die Funktion darf keine Parameter aufweisen

                Returns
                -------
                        void
                            nichts

                """	
		self.callBack = callBack

	def abmelden(self):
		self.callBack = None


        def onFaceDetected(self):
                if self.callBack == None:
                        print('no one to call')
                else:
                        val = memory.getData("FaceDetected")
                        memory.unsubscribeToEvent("FaceDetected",self.globalObjectName)
                        self.callBack()
                        memory.subscribeToEvent("FaceDetected",self.globalObjectName,"onFaceDetected")
		

