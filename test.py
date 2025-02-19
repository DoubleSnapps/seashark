from adafruit_motorkit import MotorKit

kit = MotorKit()
motor1 = kit.motor1
motor2 = kit.motor2

def drive(speed): 
    motor1.throttle(speed)
    motor2.throttle(speed)
    
def stop():
    motor1.throttle(0)
    motor2.throttle(0)
    

    
    
