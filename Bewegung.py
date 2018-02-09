from naoqi import ALProxy
import time
import almath
class Bewegung:
        def __init__(self):
#                self.motionProxy  = ALProxy("ALMotion","127.0.0.1",35495)
 #               self.postureProxy = ALProxy("ALRobotPosture","127.0.0.1",35495)
                self.motionProxy  = ALProxy("ALMotion")
                self.postureProxy = ALProxy("ALRobotPosture")

	 #Aufruf : self.greifeObjektLinks()

        def geheInGrundzustand(self):
                print('Grundzustand')
                self.postureProxy.goToPosture("Sit", 0.5)
                
	def greifeObjektLinks(self):
                print('greifeObjektLinks')
                self.postureProxy.goToPosture("Sit", 0.5)
                self.motionProxy.openHand('LHand')
                time.sleep(1.0)


                self.motionProxy.setAngles('LShoulderPitch', +1.66, 0.2)
                self.motionProxy.setAngles('LShoulderRoll', 0.39, 0.2)
                self.motionProxy.setAngles('LElbowRoll', -0.51, 0.2)
                self.motionProxy.setAngles('LElbowYaw', -1.1, 0.2)
                self.motionProxy.setAngles('LWristYaw', 0.46, 0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('LHand', 0 ,0.2)
                self.motionProxy.closeHand('LHand')

                time.sleep(2.0)

                self.motionProxy.setAngles('LShoulderPitch', +0.51, 0.2)
                self.motionProxy.setAngles('LShoulderRoll', 0.45, 0.2)
                self.motionProxy.setAngles('LElbowRoll', -0.4, 0.2)
                self.motionProxy.setAngles('LElbowYaw', -1.57, 0.2)
                self.motionProxy.setAngles('LWristYaw', -1.82, 0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('LHand', 1 ,0.2)
                self.motionProxy.openHand('LHand')

                time.sleep(2.0)
	def greifeObjektRechts(self):
                print('greifeObjektRechts')

                self.motionProxy.openHand('RHand')
                time.sleep(1.0)


                self.motionProxy.setAngles('RShoulderPitch', +1.54, 0.2)
                self.motionProxy.setAngles('RShoulderRoll', -0.29, 0.2)
                self.motionProxy.setAngles('RElbowRoll', -0.20, 0.2)
                self.motionProxy.setAngles('RElbowYaw', 1.34, 0.2)
                self.motionProxy.setAngles('RWristYaw', -0.74, 0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('RHand', 0 ,0.2)
                self.motionProxy.closeHand('RHand')
                
                self.motionProxy.setAngles('RShoulderPitch', 0.20, 0.2)
                self.motionProxy.setAngles('RShoulderRoll', -0.28, 0.2)
                self.motionProxy.setAngles('RElbowRoll', 0.22, 0.2)
                self.motionProxy.setAngles('RElbowYaw', 1.34, 0.2)
                self.motionProxy.setAngles('RWristYaw', 1.80, 0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('RHand', 1 ,0.2)
                self.motionProxy.openHand('RHand')
                                
		
        def zuruecklegenObjektLinks(self):
                print('zuruecklegenObjektLinks')
                self.motionProxy.closeHand('LHand')
                self.motionProxy.setAngles('LShoulderPitch', +1.66, 0.2)
                self.motionProxy.setAngles('LShoulderRoll', 0.39, 0.2)
                self.motionProxy.setAngles('LElbowRoll', -0.51, 0.2)
                self.motionProxy.setAngles('LElbowYaw', -1.1, 0.2)
                self.motionProxy.setAngles('LWristYaw', 0.46, 0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('LHand', 0 ,0.2)
                self.motionProxy.openHand('LHand')
                self.geheInGrundzustand()

        def zuruecklegenObjektRechts(self):
                print('zuruecklegenObjektRechts')
                self.motionProxy.closeHand('RHand')
                self.motionProxy.setAngles('RShoulderPitch', +1.54, 0.2)
                self.motionProxy.setAngles('RShoulderRoll', -0.29, 0.2)
                self.motionProxy.setAngles('RElbowRoll', -0.20, 0.2)
                self.motionProxy.setAngles('RElbowYaw', 1.34, 0.2)
                self.motionProxy.setAngles('RWristYaw', -0.74, 0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('RHand', 1 ,0.2)
                self.motionProxy.openHand('RHand')
