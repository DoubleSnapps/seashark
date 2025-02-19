import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

kit.motor1.throttle = 1.0
kit.motor3.throttle = 1.0
time.sleep(0.5)
kit.motor1.throttle = 0
kit.motor3.throttle = 0
