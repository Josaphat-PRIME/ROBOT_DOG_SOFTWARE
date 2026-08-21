from st3215 import ST3215
servo = ST3215("COM6")

servo_min = 0
servo_max = 4095


servo_ID = 2

def val_map(value , in_min , in_max, out_min , out_max ): 
    if ((in_min <= value <= in_max) or (in_min >= value >= in_max) ):
          out = ((value-in_min)*((out_max-out_min)/(in_max-in_min)))+out_min 
          return out
    else :
        return "The input value should be in [in_min , in_max]"
        return 0
    
# while True :
#     val = float(input("entrez la valeur a mapper : "))
#     print (val_map(val,360,0,servo_min,servo_max))
while True :
     
    angle = float(input("entrez la valeur de l'angle : "))

    angle_deg = int (val_map(angle , 360 , 0 , 0 , 4095))

    servo.MoveTo(servo_ID , angle_deg , speed=3000, acc=50, wait=False)