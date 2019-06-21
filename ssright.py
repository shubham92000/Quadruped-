import numpy as np
import time
import math
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16)
delay = 0.4



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
kit.servo[12].set_pulse_width_range(500,2500)
kit.servo[13].set_pulse_width_range(500,2500)
kit.servo[14].set_pulse_width_range(500,2500)
kit.servo[15].set_pulse_width_range(500,2500)
linkLength = [5.5,0,7.7,16.2]

def getInverse(x1,y1,z):
    l1 = linkLength[0]    #5.5
  #  l01= linkLength[1]    #0
    l2 = linkLength[2]    #~
    l3 = linkLength[3]    #~

    r1 = l1
    r2 = l2 
    r3 = l3
    
    x=x1*(0.707)-y1*(-0.707)
    y=x1*(-0.707)+y1*(0.707)
    
    print(x)
    print(y)   
 #   z+=l1   #Shift of Origin
    #print(2**2)
    try:
        th1 = math.atan2(y,x)
        
        A = -z
        B = r1 -(x*np.cos(th1) + y*np.sin(th1))
        D = (2*r1*(x*np.cos(th1) + y*np.sin(th1)) + (r3**2) - (r2**2) - (r1**2) -(z**2) - ((x*np.cos(th1)+y*np.sin(th1))**2) )/(2*r2)

        phi = math.atan2(B,A)
# =============================================================================
#         print(phi)
# =============================================================================

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
    
    return th1,th02,th03;


if __name__ == "__main__":

    while(1):    
                  #initialize
         TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
         kit.servo[0].angle=TH1+100                                          
         kit.servo[1].angle=TH02+100
         kit.servo[2].angle=TH03+100
             
         TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
         kit.servo[4].angle=TH1+100                                          
         kit.servo[5].angle=TH02+100
         kit.servo[6].angle=TH03+100
    #        
         TH1,TH02,TH03=getInverse(9.404,9.40,-17.2)
         kit.servo[8].angle=TH1+90                                          
         kit.servo[9].angle=TH02+90
         kit.servo[10].angle=TH03+90
         print("case 1")
         print(TH1+90)
         print(TH02+90)
         print(TH03+90)
           
         TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
         kit.servo[12].angle=TH1+90                                          
         kit.servo[13].angle=TH02+90
         kit.servo[14].angle=TH03+90
         time.sleep(1)
       
    #      # second leg
    # =============================================================================
         TH1,TH02,TH03=getInverse(9.404,14.40,-15.2)
         kit.servo[4].angle=TH1+100                                          
         kit.servo[5].angle=TH02+100
         kit.servo[6].angle=TH03+100
         time.sleep(delay)
         
         time.sleep(delay)
         
         kit.servo[8].angle=50
         time.sleep(delay)
         
         TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
         kit.servo[4].angle=TH1+100                                          
         kit.servo[5].angle=TH02+100
         kit.servo[6].angle=TH03+100
         
         
         # fourth leg 
         TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
         print("case 123")
         print(TH1+100)
         print(TH02+100)
         print(TH03+100)
         kit.servo[12].angle=TH1+90                                          
         kit.servo[13].angle=TH02+120
         kit.servo[14].angle=TH03+90
         time.sleep(delay)
         
         kit.servo[12].angle=50
         time.sleep(delay)
         kit.servo[13].angle=90
         time.sleep(delay)
         
         TH1,TH02,TH03=getInverse(9.404,14.40,-12.2)
         kit.servo[4].angle=TH1+100                                          
         kit.servo[5].angle=TH02+100
         kit.servo[6].angle=TH03+110
         time.sleep(delay)
         
         kit.servo[4].angle=50
         time.sleep(delay)
         kit.servo[5].angle=90
         
         kit.servo[13].angle=100
         time.sleep(delay)
         
         TH1,TH02,TH03=getInverse(9.404,14.40,-12.2)
         kit.servo[0].angle=TH1+100                                          
         kit.servo[1].angle=TH02+100
         kit.servo[2].angle=TH03+110
         time.sleep(delay)
    
         kit.servo[0].angle=50
         time.sleep(delay)
         kit.servo[1].angle=90
         time.sleep(delay)
         
         kit.servo[13].angle=90
         
         kit.servo[0].angle=100                                          
         kit.servo[4].angle=100
         kit.servo[8].angle=90     
         kit.servo[12].angle=90

     