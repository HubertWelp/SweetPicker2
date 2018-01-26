from naoqi import ALProxy

class Bewegung:
        def __init__(self):
#                self.motionProxy  = ALProxy("ALMotion","127.0.0.1",35495)
 #               self.postureProxy = ALProxy("ALRobotPosture","127.0.0.1",35495)
                self.motionProxy  = ALProxy("ALMotion")
                self.postureProxy = ALProxy("ALRobotPosture")

        def greifeObjektLinks(self):
                print('greifeObjektLinks')
                self.postureProxy.goToPosture("Crouch", 0.5)
				bla=3
				
        def greifeObjektRechts(self):
                print('greifeObjektRechts')
                self.postureProxy.goToPosture("Stand", 0.5)
                bla=1ss

        def zuruecklegenObjekt(self):
                print('zuruecklegenObjekt')
                self.postureProxy.goToPosture("Sit", 0.5)
