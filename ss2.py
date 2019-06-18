#import sys
#sys.path.insert(0, "..")
import numpy as np
#import constants as k
# =============================================================================
import time
# =============================================================================
import math
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16)
delay = 1.0



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

def getInverse(x1,y1,z):
    l1 = linkLength[0]    #5.5
    l01= linkLength[1]    #0
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
    
    #initialize
    TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)

    kit.servo[0].angle=TH1+100                                          
    kit.servo[1].angle=TH02+100
    kit.servo[2].angle=TH03+100
    
    TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)

    kit.servo[4].angle=TH1+100                                          
    kit.servo[5].angle=TH02+100
    kit.servo[6].angle=TH03+100
   
    TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)

    kit.servo[8].angle=TH1+90                                          
    kit.servo[9].angle=TH02+90
    kit.servo[10].angle=TH03+90
    
   
    TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)

    kit.servo[12].angle=TH1+90                                          
    kit.servo[13].angle=TH02+90
    kit.servo[14].angle=TH03+90
    time.sleep(delay)
 
    # first leg
    TH1,TH02,TH03=getInverse(9.404,14.40,-12.2)

    print(TH1)
    print(TH02)
    print(TH03)
    
    kit.servo[0].angle=TH1+100                                          
    kit.servo[1].angle=TH02+100
    kit.servo[2].angle=TH03+100
    time.sleep(delay)
    
    TH1,TH02,TH03=getInverse(-4.404,17.40,-12.2)

    kit.servo[0].angle=TH1+100                                          
    kit.servo[1].angle=TH02+100
    kit.servo[2].angle=TH03+100
    time.sleep(delay)
    
    TH1,TH02,TH03=getInverse(-4.404,9.40,-16.2)

    kit.servo[0].angle=TH1+100                                          
    kit.servo[1].angle=TH02+100
    kit.servo[2].angle=TH03+100
    time.sleep(delay)
    
    
# =============================================================================
#     #second leg
#     
#     TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
# 
#     kit.servo[4].angle=TH1+100                                          
#     kit.servo[5].angle=TH02+100
#     kit.servo[6].angle=TH03+100
#     time.sleep(delay)
# =============================================================================
    # second leg
    TH1,TH02,TH03=getInverse(9.404,14.40,-12.2)

    print(TH1)
    print(TH02)
    print(TH03)
    
    kit.servo[4].angle=TH1+100                                          
    kit.servo[5].angle=TH02+100
    kit.servo[6].angle=TH03+100
    time.sleep(delay)
    
    TH1,TH02,TH03=getInverse(17.404,-2.40,-12.2)

    kit.servo[4].angle=TH1+100                                          
    kit.servo[5].angle=TH02+100
    kit.servo[6].angle=TH03+100
    time.sleep(delay)
    
    TH1,TH02,TH03=getInverse(9.404,-2.40,-16.2)

    kit.servo[4].angle=TH1+100                                          
    kit.servo[5].angle=TH02+100
    kit.servo[6].angle=TH03+100
    time.sleep(delay)

      
    TH1=TH1+100
    TH02=TH02+100
    TH03=TH03+100  
# =============================================================================
#     
#     #third leg
#     TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
# 
#     kit.servo[8].angle=TH1+90                                          
#     kit.servo[9].angle=TH02+90
#     kit.servo[10].angle=TH03+90
#     time.sleep(delay)
#      
#     #fourth leg
#     
#     TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
# 
#     kit.servo[12].angle=TH1+90                                          
#     kit.servo[13].angle=TH02+90
#     kit.servo[14].angle=TH03+90
#     time.sleep(delay)
# =============================================================================
    
    # first leg extend
    TH1,TH02,TH03=getInverse(-4.404,17.40,-12.2)

    kit.servo[0].angle=TH1+100                                          
    kit.servo[1].angle=TH02+100
    kit.servo[2].angle=TH03+100
    time.sleep(delay)
    
    TH1,TH02,TH03=getInverse(25.404,9.404,-12.2)
      
    print(TH1)
    print(TH02)
    print(TH03)
    kit.servo[0].angle=TH1+100                                          
    kit.servo[1].angle=TH02+100
    kit.servo[2].angle=TH03+100
    time.sleep(delay)
      
        
    TH1,TH02,TH03=getInverse(15.404,15.404,-16.2)
    
        
    print(TH1)
    print(TH02)
    print(TH03)
    
    kit.servo[0].angle=TH1+100                                          
    kit.servo[1].angle=TH02+100
    kit.servo[2].angle=TH03+100
    time.sleep(delay)

     # push by remaining legs
     
     
    TH1,TH02,TH03=getInverse(0.404,20.404,-16.2)
    
    print(TH1)
    print(TH02)
    print(TH03) 
    
    kit.servo[0].angle=TH1+90                                          
    kit.servo[1].angle=TH02+90
    kit.servo[2].angle=TH03+90
   
    
    
    
    TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)

    kit.servo[4].angle=TH1+100                                          
    kit.servo[5].angle=TH02+100
    kit.servo[6].angle=TH03+100
   
    
    
    
      
    TH1,TH02,TH03=getInverse(13.404,0.40,-16.2)
  
    print(TH1+90)
    print(TH02+90)
    print(TH03+90) 
    kit.servo[8].angle=TH1+90                                          
    kit.servo[9].angle=TH02+90
    kit.servo[10].angle=TH03+90
   
    
    
    TH1,TH02,TH03=getInverse(15.404,15.404,-16.2)

    kit.servo[12].angle=TH1+90                                          
    kit.servo[13].angle=TH02+90
    kit.servo[14].angle=TH03+90
    
    
    
       #third leg (mirror of first leg)
    TH1,TH02,TH03=getInverse(17.404,9.40,-12.2)

    kit.servo[8].angle=TH1+90                                          
    kit.servo[9].angle=TH02+90
    kit.servo[10].angle=TH03+90
    time.sleep(delay)
    
    TH1,TH02,TH03=getInverse(20.404,-4.40,-12.2)
    
    print(TH1+90)
    print(TH02+90)
    print(TH03+90)
    
    kit.servo[8].angle=TH1+90                                          
    kit.servo[9].angle=TH02+90
    kit.servo[10].angle=TH03+90
    time.sleep(delay)
    
    TH1,TH02,TH03=getInverse(20.404,-4.40,-16.2)

    kit.servo[8].angle=TH1+90                                          
    kit.servo[9].angle=TH02+90
    kit.servo[10].angle=TH03+90
    time.sleep(delay)
    
      # fourth leg(mirror of second leg)
    TH1,TH02,TH03=getInverse(9.404,20.40,-12.2)

    print(TH1+90)
    print(TH02+90)
    print(TH03+90)
    
    kit.servo[12].angle=TH1+90                                          
    kit.servo[13].angle=TH02+90
    kit.servo[14].angle=TH03+90
    time.sleep(delay)
    
    TH1,TH02,TH03=getInverse(2.404,20.40,-12.2)
    
    print(TH1+90)
    print(TH02+90)
    print(TH03+90)
    kit.servo[12].angle=TH1+90                                          
    kit.servo[13].angle=TH02+90
    kit.servo[14].angle=TH03+90
    time.sleep(delay)
    
    TH1,TH02,TH03=getInverse(-4.404,17.404,-16.2)

    kit.servo[12].angle=TH1+90                                          
    kit.servo[13].angle=TH02+90
    kit.servo[14].angle=TH03+90
    time.sleep(delay)

      
    TH1=TH1+100
    TH02=TH02+100
    TH03=TH03+100  
   
    #first leg (mirror of third leg) 
    TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)

    kit.servo[0].angle=TH1+100                                          
    kit.servo[1].angle=TH02+100
    kit.servo[2].angle=TH03+100
    
    #second leg (mirror of fourth leg) 
    TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)

    kit.servo[4].angle=TH1+100                                          
    kit.servo[5].angle=TH02+100
    kit.servo[6].angle=TH03+100
    time.sleep(delay)
    
     # third leg extend
    TH1,TH02,TH03=getInverse(10.944652706,-0.000273616317707,21.6447322148)

    kit.servo[8].angle=TH1+90                                          
    kit.servo[9].angle=TH02+90
    kit.servo[10].angle=TH03+90
    time.sleep(delay)
    
    TH1,TH02,TH03=getInverse(25.404,9.404,-12.2)
      
    print(TH1)
    print(TH02)
    print(TH03)
    kit.servo[8].angle=TH1+90                                          
    kit.servo[9].angle=TH02+90
    kit.servo[10].angle=TH03+90
    time.sleep(delay)
      
        
    TH1,TH02,TH03=getInverse(15.404,15.404,-16.2)
    
        
    print(TH1)
    print(TH02)
    print(TH03)
    
    kit.servo[8].angle=TH1+90                                          
    kit.servo[9].angle=TH02+90
    kit.servo[10].angle=TH03+90
    time.sleep(delay)
    
    # push by remaining legs(mirror of first push
     
     
    TH1,TH02,TH03=getInverse(0.404,20.404,-16.2)
    
    print(TH1)
    print(TH02)
    print(TH03)
    
    kit.servo[8].angle=TH1+90                                          
    kit.servo[9].angle=TH02+90
    kit.servo[10].angle=TH03+90
   
    
    
    
    TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)

    kit.servo[12].angle=TH1+90                                          
    kit.servo[13].angle=TH02+90
    kit.servo[14].angle=TH03+90
   
    
    
    
      
    TH1,TH02,TH03=getInverse(13.404,0.40,-16.2)
  
    print(TH1+90)
    print(TH02+90)
    print(TH03+90) 
    kit.servo[0].angle=TH1+100                                          
    kit.servo[1].angle=TH02+100
    kit.servo[2].angle=TH03+100
   
    
    
    TH1,TH02,TH03=getInverse(15.404,15.404,-16.2)

    kit.servo[4].angle=TH1+100                                          
    kit.servo[5].angle=TH02+100
    kit.servo[6].angle=TH03+100
    
    
#     kit.servo[3].angle=TH1+10
#     kit.servo[4].angle=TH1+90
#     kit.servo[5].angle=TH1+90
# =============================================================================
    #kit.servo[6].angle=TH1+90
     #kit.servo[7].angle=TH1+90
     #kit.servo[8].angle=TH1+90
     #kit.servo[9].angle=TH1+90
     #kit.servo[10].angle=TH1+90
     #kit.servo[11].angle=TH1+90
     #kit.servo[12].angle=TH1+90
     #kit.servo[13].angle=TH1+90
     #kit.servo[ 14].angle=TH1+90
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
     
