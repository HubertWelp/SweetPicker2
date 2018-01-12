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
        self.topf_path = "C:\\Users\\ITL.NAO.1\\Documents\\SWT-SP2\\SweetPicker2\\begruessung_ged.top"
#        self.topf_path = self.topf_path.decode('utf-8')
#        self.topic = self.dialog_p.loadTopic(self.topf_path.encode('utf-8'))
#        self.topf_path = "/home/nao/begruessung_ged.top"
        global memory
        memory = ALProxy("ALMemory")
        print(self.globalObjectName)
        memory.subscribeToEvent("retDialog",self.globalObjectName,"onReturnDialog")
        self.ret = 0
        
    def begruesse(self):
        self.ret = -1
        # Start dialog
        self.topic = self.dialog_p.loadTopic(self.topf_path)
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

    def onReturnDialog(self, *_args):
        """ this method has to be bound because it is a callback. Therefore this comment. """
        r = memory.getData("retDialog")
        self.ret = int(r)
        print(self.ret)
        print("onReturnDialog")
