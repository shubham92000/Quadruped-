import sys
sys.path.insert(0, "..")
import numpy as np
#import constants as k
import math
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16)

x=29.5
y=0
z=0

l1=5.6
l2=7.7
l3=16.2

r1 = l1
r2 = l2 
r3 = l3

th1 = math.atan2(y,x)

A = -z
B = r1 -(x*np.cos(th1) + y*np.sin(th1))
D = (2*r1*(x*np.cos(th1) + y*np.sin(th1)) + (r3**2) - (r2**2) - (r1**2) -(z**2) - ((x*np.cos(th1)+y*np.sin(th1))**2) )/(2*r2)
phi = math.atan2(B,A)

th02 = -phi + math.atan2(D , + math.pow(((A**2)+(B**2) - (D**2)),0.5)  )
th12 = -phi + math.atan2(D , - math.pow(((A**2)+(B**2) - (D**2)),0.5)  )
th03 = np.arctan2( z-r2*np.sin(th02) , x*np.cos(th1) + y*np.sin(th1) - r2*np.cos(th02) -r1 ) -th02 
th13 = np.arctan2( z-r2*np.sin(th12) , x*np.cos(th1) + y*np.sin(th1) - r2*np.cos(th12) -r1 ) -th12
   
th1 *=180/np.pi
th02*=180/np.pi
th12*=180/np.pi
th03*=180/np.pi
th13*=180/np.pi

print(th1)
print(th02)
print(th12)
print(th03)
print(th13)  
    
 #   return 0,0,0,False

if __name__=="__main__":

    kit.servo[0].angle = th1
    kit.servo[4].angle = th02
    kit.servo[8].angle = th13

