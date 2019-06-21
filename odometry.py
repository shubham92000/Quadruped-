import numpy as np
import time
import math
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16)
delay = 0.2



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
    
     x=float(input("enter x coordinate: "))
     y=float(input("enter y coordinate: "))
     x=x/14
    
     print("NO OF STEPS IS: " + str(x))
     counter_x=0
     counter_y=0
     i=1  
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
    
       
     TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
     kit.servo[12].angle=TH1+90                                          
     kit.servo[13].angle=TH02+90
     kit.servo[14].angle=TH03+90
     time.sleep(4)
       
     kit.servo[13].angle=110
     time.sleep(delay)
     kit.servo[1].angle=65
     time.sleep(delay) 
     
     #firstleg
     TH1,TH02,TH03=getInverse(9.404,14.40,-12.2)
     kit.servo[0].angle=TH1+100                                          
     kit.servo[1].angle=TH02+100
     kit.servo[2].angle=TH03+100
     time.sleep(delay)
    # #         
     TH1,TH02,TH03=getInverse(-4.404,17.40,-12.2)
     kit.servo[0].angle=TH1+100                                          
     kit.servo[1].angle=TH02+100
     kit.servo[2].angle=TH03+100
     time.sleep(delay)
    # #         
     TH1,TH02,TH03=getInverse(-4.404,9.40,-16.2)
     kit.servo[0].angle=TH1+100                                          
     kit.servo[1].angle=TH02+100
     kit.servo[2].angle=TH03+100
     time.sleep(delay)

    # #         # second leg
     TH1,TH02,TH03=getInverse(9.404,14.40,-12.2)
     kit.servo[4].angle=TH1+100                                          
     kit.servo[5].angle=TH02+100
     kit.servo[6].angle=TH03+100
     time.sleep(delay)
    # #         
     TH1,TH02,TH03=getInverse(17.404,-2.40,-12.2)
     kit.servo[4].angle=TH1+100                                          
     kit.servo[5].angle=TH02+100
     kit.servo[6].angle=TH03+100
     time.sleep(delay)
    # #         
     TH1,TH02,TH03=getInverse(9.404,-2.40,-16.2)
    
     print(TH1+100)
     print(TH02+100)
     print(TH03+100)
     
     kit.servo[4].angle=TH1+100                                          
     kit.servo[5].angle=TH02+100
     kit.servo[6].angle=TH03+100
     time.sleep(delay)
         
     while(i<=x):
             # first leg extend
         TH1,TH02,TH03=getInverse(-4.404,20.40,-9.404)
      
         print("case 7")
    
         print(TH1+100)
         print(TH02+100)
         print(TH03+100)
         kit.servo[0].angle=TH1+100                                          
         kit.servo[1].angle=TH02+100
         kit.servo[2].angle=TH03+100
         time.sleep(delay)
    # #         
         TH1,TH02,TH03=getInverse(20.404,9.404,-9.404)
         print("case 4")
    
         print(TH1+100)
         print(TH02+100)
         print(TH03+100)
         kit.servo[0].angle=TH1+100                                          
         kit.servo[1].angle=TH02+100
         kit.servo[2].angle=TH03+100
         time.sleep(delay)
    # #           
    #           
         TH1,TH02,TH03=getInverse(12.404,7.404,-16.2)
         print("case 5")
    
         print(TH1+100)
         print(TH02+100)
         print(TH03+100)
         kit.servo[0].angle=TH1+100                                          
         kit.servo[1].angle=TH02+100
         kit.servo[2].angle=TH03+100
         time.sleep(delay)
         
         #pushgfhhgjgjughjghjghjgh
         
               # leg 1   
         TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
         kit.servo[0].angle=TH1+100                                          
         kit.servo[1].angle=TH02+100
         kit.servo[2].angle=TH03+100
             
         
         
         #leg 2
         TH1,TH02,TH03=getInverse(9.404,-2.40,-16.2)
         print("case 275255828")
         print(TH1+150)
         print(TH02+100)
         print(TH03+100)
         
         kit.servo[4].angle=TH1+150                                          
         kit.servo[5].angle=TH02+100
         kit.servo[6].angle=TH03+100
         
         #leg 3
         TH1,TH02,TH03=getInverse(9.404,9.40,-18.2)
         print("case 6")
         print(TH1+50)
         print(TH02+90)
         print(TH03+90)
         kit.servo[8].angle=TH1+50                                          
         kit.servo[9].angle=TH02+90
         kit.servo[10].angle=TH03+90
         
         #leg 4
         TH1,TH02,TH03=getInverse(5.404,5.40,-16.2)
         
         print("case 1")
         print(TH1+90)
         print(TH02+90)
         print(TH03+140)
         
         kit.servo[12].angle=TH1+90                                          
         kit.servo[13].angle=TH02+90
         kit.servo[14].angle=TH03+140
         time.sleep(delay)
        
         
         #third leg (mirror of first leg)
         TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
         kit.servo[8].angle=TH1+90                                          
         kit.servo[9].angle=TH02+90
         kit.servo[10].angle=TH03+90
          #fourth leg (mirror of second leg)    
         TH1,TH02,TH03=getInverse(9.404,9.40,-16.2)
         kit.servo[8].angle=TH1+90                                          
         kit.servo[9].angle=TH02+90
         kit.servo[10].angle=TH03+90
         
         kit.servo[9].angle=80
         kit.servo[5].angle=125
         time.sleep(delay)
         
    # third leg(mirror of second leg INSIDE)
          
         TH1,TH02,TH03=getInverse(16.404,9.40,-12.2)
         
         kit.servo[8].angle=TH1+90                                          
         kit.servo[9].angle=TH02+90
         kit.servo[10].angle=TH03+90
         time.sleep(delay)
    # #         
         TH1,TH02,TH03=getInverse(20.404,-0.40,-12.2)
        
         kit.servo[8].angle=TH1+90                                          
         kit.servo[9].angle=TH02+90
         kit.servo[10].angle=TH03+90
         time.sleep(delay)
    # #         
         TH1,TH02,TH03=getInverse(16.404,0.404,-17.2)
         kit.servo[8].angle=TH1+90                                          
         kit.servo[9].angle=TH02+90
         kit.servo[10].angle=TH03+90
         time.sleep(delay)
         
         kit.servo[5].angle=97       
    # #  

    # #  # fourth leg(mirror of second leg INSIDE)
         TH1,TH02,TH03=getInverse(16.404,9.40,-12.2)
         kit.servo[12].angle=TH1+90                                          
         kit.servo[13].angle=TH02+90
         kit.servo[14].angle=TH03+90
         time.sleep(delay)
    # #         
         TH1,TH02,TH03=getInverse(-2.404,20.40,-12.2)
         print(TH1+90)
         print(TH02+90)
         print(TH03+90)
         kit.servo[12].angle=TH1+90                                          
         kit.servo[13].angle=TH02+90
         kit.servo[14].angle=TH03+90
         time.sleep(delay)
    # #         
         TH1,TH02,TH03=getInverse(-0.404,13.40,-16.2)
        
         print(TH1+90)
         print(TH02+90)
         print(TH03+90)
         
         kit.servo[12].angle=TH1+90                                          
         kit.servo[13].angle=TH02+90
         kit.servo[14].angle=TH03+90
         time.sleep(delay) 
         
          # third leg extend(mirror of first leg)
         TH1,TH02,TH03=getInverse(20.45,0.40,-12.404)
         print(TH1+90)
         print(TH02+90)
         print(TH03+90)
         kit.servo[8].angle=TH1+90                                          
         kit.servo[9].angle=TH02+90
         kit.servo[10].angle=TH03+90
         time.sleep(delay)            
         TH1,TH02,TH03=getInverse(20.404,9.404,-9.404)
         print("case 4")
         print(TH1+90)
         print(TH02+90)
         print(TH03+90)  
         kit.servo[8].angle=TH1+90                                          
         kit.servo[9].angle=TH02+90
         kit.servo[10].angle=TH03+90
         time.sleep(delay)
              
         TH1,TH02,TH03=getInverse(11.404,14.404,-16.2)
         print("case 5")
         print(TH1+90)
         print(TH02+90)
         print(TH03+90)
         kit.servo[8].angle=TH1+90                                          
         kit.servo[9].angle=TH02+90
         kit.servo[10].angle=TH03+90
         time.sleep(delay)
          
         #pushgfhhgjgjughjghjghjgh
          
                # leg 3   
         TH1,TH02,TH03=getInverse(9.404,9.404,-18.2)
         kit.servo[8].angle=TH1+90                                          
         kit.servo[9].angle=TH02+90
         kit.servo[10].angle=TH03+90
         
          
          
          #leg 1
         TH1,TH02,TH03=getInverse(9.404,-2.40,-16.2)
         print("case 8")
         print(TH1+200)
         print(TH02+100)
         print(TH03+100)
         
         kit.servo[0].angle=TH1+200                                          
         kit.servo[1].angle=TH02+100
         kit.servo[2].angle=TH03+100
          
          #leg 4
         TH1,TH02,TH03=getInverse(-0.404,13.40,-16.2)
         print("case 6")
         print(TH1+50)
         print(TH02+90)
         print(TH03+90)
         kit.servo[12].angle=TH1+50                                          
         kit.servo[13].angle=TH02+90
         kit.servo[14].angle=TH03+90
          
          #leg 2
         TH1,TH02,TH03=getInverse(7.404,7.40,-14.2)
         kit.servo[4].angle=TH1+90                                          
         kit.servo[5].angle=TH02+90
         kit.servo[6].angle=TH03+140
         #time.sleep(delay)
         
         #jkdsngjk
         
         TH1,TH02,TH03=getInverse(9.404,14.40,-12.2)
         kit.servo[4].angle=TH1+100                                          
         kit.servo[5].angle=TH02+100
         kit.servo[6].angle=TH03+100
         time.sleep(delay)
    # #         
         TH1,TH02,TH03=getInverse(17.404,-2.40,-12.2)
         kit.servo[4].angle=TH1+100                                          
         kit.servo[5].angle=TH02+100
         kit.servo[6].angle=TH03+100
         time.sleep(delay)
    # #         
         TH1,TH02,TH03=getInverse(9.404,-2.40,-16.2)
        
         print(TH1+100)
         print(TH02+100)
         print(TH03+100)
         
         kit.servo[4].angle=TH1+100                                          
         kit.servo[5].angle=TH02+100
         kit.servo[6].angle=TH03+100
         time.sleep(delay)         
             
         i=i+1