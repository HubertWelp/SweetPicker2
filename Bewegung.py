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
                self.postureProxy.goToPosture("Crouch", 0.5)
                
	def greifeObjektLinks(self):
                print('greifeObjektLinks')
                self.motionProxy.wakeUp()
                self.postureProxy.goToPosture("Crouch", 0.5)
                self.motionProxy.setAngles('LShoulderPitch', +0.96, 0.2)
                self.motionProxy.setAngles('LShoulderRoll', 0.019, 0.2)
                self.motionProxy.setAngles('LElbowYaw', -1.5, 0.2)
                self.motionProxy.setAngles('LElbowRoll', 0.2, 0.2)
                self.motionProxy.setAngles('LWristYaw', +1.5, 0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('LHand', 0 ,0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('LShoulderPitch', +0.96, 0.2)
                self.motionProxy.setAngles('LShoulderRoll', 0.019, 0.2)
                self.motionProxy.setAngles('LElbowYaw', -1.5, 0.2)
                self.motionProxy.setAngles('LElbowRoll', -1.12, 0.2)
                self.motionProxy.setAngles('LWristYaw', -1.5, 0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('LHand', 1 ,0.2)
	def greifeObjektRechts(self):
		print('greifeObjektRechts')
		self.motionProxy.wakeUp()
		self.postureProxy.goToPosture("Crouch", 0.5)
		self.motionProxy.openHand('RHand')
		    
		time.sleep(2.0)
			
	       	self.motionProxy.setAngles('RShoulderPitch', +0.67, 0.2)
                self.motionProxy.setAngles('RShoulderRoll', -0.3, 0.2)
                self.motionProxy.setAngles('RElbowYaw', -1.46, 0.2)
                self.motionProxy.setAngles('RElbowRoll', 0.61, 0.2)
                self.motionProxy.setAngles('RWristYaw', +1.32, 0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('RHand', 0 ,0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('RShoulderPitch', +0.43, 0.2)
                self.motionProxy.setAngles('RShoulderRoll', 0.17, 0.2)
                self.motionProxy.setAngles('RElbowYaw',  1.77, 0.2)
                self.motionProxy.setAngles('RElbowRoll', 0.60, 0.2)
                self.motionProxy.setAngles('RWristYaw', +1.32, 0.2)
                time.sleep(2.0)
                self.motionProxy.setAngles('RHand', 1 ,0.2)
			
		
        def zuruecklegenObjektLinks(self):
                print('zuruecklegenObjektLinks')
                self.postureProxy.goToPosture("Sit", 0.5)
                self.geheInGrundzustand()

        def zuruecklegenObjektRechts(self):
                print('zuruecklegenObjektRechts')
                self.postureProxy.goToPosture("Sit", 0.5)
                self.geheInGrundzustand()

