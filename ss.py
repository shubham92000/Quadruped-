from adafruit_servokit import ServoKit
kit= ServoKit(channels=16)

kit.servo[0].angle= 100
kit.servo[1].angle= 100
kit.servo[2].angle=100 
kit.servo[12].angle= 0

