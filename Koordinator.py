import time
import sys
from Gesichtserkenner import Gesichtserkenner
from NutzerDialog import NutzerDialog
from Bewegung import Bewegung
from naoqi import ALBroker
from optparse import OptionParser

class Koordinator:

    def __init__(self, name, gesichtserkenner,begruesser):
        self.name = "Welp"
        self.ge = gesichtserkenner
        self.ge.anmelden(self.onPersonErkannt)
        self.nd = begruesser
        self.bw = Bewegung()
        self.bw.geheInGrundzustand()

    def onPersonErkannt(self):
        print('Gesicht erkannt')
        self.ge.abmelden()
        ret = self.nd.begruesse()
        print('ret=',ret)
        if ret==0:
            print('keine Antowrt')
        if (ret==1):
            print('Mars')  
            self.bw.greifeObjektLinks()
            self.nd.ueberreiche()
            # Warte noch eine Sicherheitspause, bevor die Hand geschlossen wird
            dialogDauer = 10.0
            dialogStart = time.time()
            while time.time()-dialogStart<dialogDauer:
                time.sleep(1)
            self.bw.zuruecklegenObjektLinks()
        if (ret==2):
            print('Milky Way')
            self.bw.greifeObjektRechts()
            self.nd.ueberreiche()
            # Warte noch eine Sicherheitspause, bevor die Hand geschlossen wird
            dialogDauer = 10.0
            dialogStart = time.time()
            while time.time()-dialogStart<dialogDauer:
                time.sleep(1)
            self.bw.zuruecklegenObjektRechts()

        dialogDauer = 20.0
        dialogStart = time.time()
        while time.time()-dialogStart<dialogDauer:
            time.sleep(1)
        self.ge.anmelden(self.onPersonErkannt)
        
    def ausgeben(self):
        print(self.name)
		

NAO_IP = "192.168.76.101"
gesichtserkenner = None
begruesser = None

def main():
    """ Main entry point

    """
    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port


    # Warning: gesichtserkenner must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global gesichtserkenner
    global begruesser
    gesichtserkenner = Gesichtserkenner("gesichtserkenner")
    begruesser = NutzerDialog("begruesser")
    k=Koordinator("BLA", gesichtserkenner,begruesser)
#    gesichtserkenner.onFaceDetected()
#    gesichtserkenner.run()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)



if __name__ == "__main__":
    main()


