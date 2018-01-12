from naoqi import ALProxy

class Bewegung:
        def __init__(self):
#                self.motionProxy  = ALProxy("ALMotion","127.0.0.1",35495)
 #               self.postureProxy = ALProxy("ALRobotPosture","127.0.0.1",35495)
                self.motionProxy  = ALProxy("ALMotion")
                self.postureProxy = ALProxy("ALRobotPosture")

        def greifeObjektLinks(self):
                self.postureProxy.goToPosture("Crouch", 0.5)

        def greifeObjektRechts(self):
                bla=1
