from st3215 import ST3215
from LOCOMOTION import Inverse_Kinematics
servo = ST3215("COM6")

servo_min = 0
servo_max = 4095

while True : 
    x, z = float (input ("valeur de x : ")) , float (input ("valeur de z : ")) 


    theta1 , theta2  = Inverse_Kinematics.angles(x, z)
    
    theta2 = 2048 + ((theta2-180)*(26/15)*(4095/360))

    servo_ID_3 = 3
    servo_ID_2 = 2

    def val_map(value , in_min , in_max, out_min , out_max ): 
        if ((in_min <= value <= in_max) or (in_min >= value >= in_max) ):
            out = ((value-in_min)*((out_max-out_min)/(in_max-in_min)))+out_min 
            return out
        else :
            return "The input value should be in [in_min , in_max]"
            return 0

   
    angle_deg_2 = int (val_map(theta1 , 360 , 0 , 0 , 4095))

    print ("valeur de thetha_2 ", angle_deg_2)
    servo.MoveTo(servo_ID_2 , angle_deg_2 , speed=4000, acc=50, wait=False)
    servo.MoveTo(servo_ID_3 ,  int(theta2)   , speed=4000, acc=50, wait=False)