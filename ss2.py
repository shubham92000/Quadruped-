#import sys
#sys.path.insert(0, "..")
import numpy as np
#import constants as k
import time
import math
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16)
delay = 1
kit.servo[0].set_pulse_width_range(500,2500)
kit.servo[1].set_pulse_width_range(500,2500)
kit.servo[2].set_pulse_width_range(500,2500)
kit.servo[3].set_pulse_width_range(500,2500)
kit.servo[4].set_pulse_width_range(500,2500)
kit.servo[5].set_pulse_width_range(500,2500)
kit.servo[6].set_pulse_width_range(500,2500)
kit.servo[7].set_pulse_width_range(500,2500)
kit.servo[8].set_pulse_width_range(500,2500)
kit.servo[9].set_pulse_width_range(500,2500)
kit.servo[10].set_pulse_width_range(500,2500)
kit.servo[11].set_pulse_width_range(500,2500)
#kit.servo[0].set_pulse_width_range(500,2500)
#kit.servo[4].set_pulse_width_range(500,2500)
#kit.servo[9].set_pulse_width_range(500,2500)
linkLength = [5.5,0,7.7,16.2]

def getInverse(x,y,z):
    l1 = linkLength[0]    #5.5
    l01= linkLength[1]    #0
    l2 = linkLength[2]    #~
    l3 = linkLength[3]    #~

    r1 = l1
    r2 = l2 
    r3 = l3

 #   z+=l1   #Shift of Origin 
    
    #print(2**2)

    try:
        th1 = math.atan2(y,x)

        A = -z
        B = r1 -(x*np.cos(th1) + y*np.sin(th1))
        D = (2*r1*(x*np.cos(th1) + y*np.sin(th1)) + (r3**2) - (r2**2) - (r1**2) -(z**2) - ((x*np.cos(th1)+y*np.sin(th1))**2) )/(2*r2)

        phi = math.atan2(B,A)

        # print(A,B,D)

        th02 = -phi + math.atan2(D , + math.pow(((A**2)+(B**2) - (D**2)),0.5)  )
        th12 = -phi + math.atan2(D , - math.pow(((A**2)+(B**2) - (D**2)),0.5)  )
        
        th03 = np.arctan2( z-r2*np.sin(th02) , x*np.cos(th1) + y*np.sin(th1) - r2*np.cos(th02) -r1 ) -th02 ;
        th13 = np.arctan2( z-r2*np.sin(th12) , x*np.cos(th1) + y*np.sin(th1) - r2*np.cos(th12) -r1 ) -th12 ;

        th1 *=180/np.pi
        th02*=180/np.pi
        th12*=180/np.pi
        th03*=180/np.pi
        th13*=180/np.pi

        #th03+=90
      #  th13+=90    
    except:
        return 0,0,0; #Return Not Possible
    
    return th1,th12,th13;


if __name__ == "__main__":
    TH1,TH02,TH03=getInverse(29.5,0,0)
    kit.servo[0].angle=TH1+170                                                        
    kit.servo[1].angle=TH1+100
    kit.servo[2].angle=TH1+100
    kit.servo[3].angle=TH1+10
    kit.servo[4].angle=TH1+90
    kit.servo[5].angle=TH1+90
    #kit.servo[6].angle=TH1+90
     #kit.servo[7].angle=TH1+90
     #kit.servo[8].angle=TH1+90
     #kit.servo[9].angle=TH1+90
     #kit.servo[10].angle=TH1+90
     #kit.servo[11].angle=TH1+90
     #kit.servo[12].angle=TH1+90
     #kit.servo[13].angle=TH1+90
     #kit.servo[14].angle=TH1+90
     #kit.servo[15].angle=TH1+90
   # int i=0
    #int servo = [0 , 1 , 3]
   # for i in servo:
    #while(1):        
#step1
# =============================================================================
#         kit.servo[0].angle=TH1+100 
#         kit.servo[1].angle=TH1+100   
#         kit.servo[2].angle=TH1+20  
#         time.sleep(delay)
#         kit.servo[0].angle=TH1+100
#         kit.servo[1].angle=TH1+130
#         kit.servo[2].angle=TH1+20
#         time.sleep(delay)
#         kit.servo[0].angle=TH1+170
#         kit.servo[1].angle=TH1+130
#         kit.servo[2].angle=TH1+20
#         time.sleep(delay)
#         kit.servo[0].angle=TH1+170
#         kit.servo[1].angle=TH1+100
#         kit.servo[2].angle=TH1+20
#         time.sleep(delay)   
# #step2      
#         kit.servo[3].angle=TH1+100 
#         kit.servo[4].angle=TH1+100   
#         kit.servo[5].angle=TH1+1  
#         time.sleep(delay)
#         kit.servo[3].angle=TH1+100
#         kit.servo[4].angle=TH1+130
#         kit.servo[5].angle=TH1+1
#         time.sleep(delay)
#         kit.servo[3].angle=TH1+45
#         kit.servo[4].angle=TH1+130
#         kit.servo[5].angle=TH1+1
#         time.sleep(delay)
#         kit.servo[3].angle=TH1+45
#         kit.servo[4].angle=TH1+100
#         kit.servo[5].angle=TH1+1
#         time.sleep(delay)
# #step3
#         kit.servo[6].angle=TH1+90
#         kit.servo[7].angle=TH1+90
#         kit.servo[8].angle=TH1+1
#         time.sleep(delay)
#         kit.servo[9].angle=TH1+90
#         kit.servo[10].angle=TH1+90
#         kit.servo[11].angle=TH1+1
#         time.sleep(delay)
# 
#         kit.servo[0].angle=TH1+170
#         kit.servo[1].angle=TH1+130
#         kit.servo[2].angle=TH1+20
#         time.sleep(delay)
#         kit.servo[0].angle=TH1+100
#         kit.servo[1].angle=TH1+130
#         kit.servo[2].angle=TH1+20
#         time.sleep(delay)
#         kit.servo[0].angle=TH1+100
#         kit.servo[1].angle=TH1+100
#         kit.servo[2].angle=TH1+30
#         time.sleep(delay)
#  #    TH1=TH1-90ee
# =============================================================================
  #   TH02=TH02-90
   #  TH03=TH03-90
    # print(TH1)
  #   print(TH02)
   #  print(TH03)


