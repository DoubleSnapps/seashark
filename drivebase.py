from adafruit_motorkit import MotorKit

class Drivebase:
    def __init__(self):
        self.kit = MotorKit()
        self.motorL = self.kit.motor1
        self.motorR = self.kit.motor3

    def drive(self, speed): 
        self.motorL.throttle = speed 
        self.motorR.throttle = speed
        
    def turnL(self, speed):
        self.motorL.throttle = speed
        self.motorR.throttle = -speed
        
    def turnR(self, speed):
        self.motorL.throttle = -speed
        self.motorR.throttle = speed
        
    def stop(self):
        self.motorL.throttle = 0
        self.motorR.throttle = 0
