from st3215 import ST3215
from LOCOMOTION import Inverse_Kinematics
servo = ST3215("COM6")

servo_min = 0
servo_max = 4095


theta1 , theta2  = Inverse_Kinematics.angles(100 , 100)

theta2 = (theta2*27)/15

servo_ID = 3

def val_map(value , in_min , in_max, out_min , out_max ): 
    if ((in_min <= value <= in_max) or (in_min >= value >= in_max) ):
          out = ((value-in_min)*((out_max-out_min)/(in_max-in_min)))+out_min 
          return out
    else :
        return "The input value should be in [in_min , in_max]"
        return 0
while True : 
    angle = int (input ("valeur : ") ) 
    angle = (angle*15)/26
    #angle_deg = int (val_map(theta1 , 360 , 0 , 0 , 4095))
    angle_deg2 = int (val_map(angle, 0 , (360*15/26), 0 , 4095))

    #servo.MoveTo(servo_ID , angle_deg , speed=2000, acc=50, wait=False)
    servo.MoveTo(servo_ID , angle_deg2 , speed=2000, acc=50, wait=False)