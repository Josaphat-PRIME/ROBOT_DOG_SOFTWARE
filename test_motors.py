from st3215 import ST3215
servo_min = 0
servo_max = 4095


servo = ST3215("COM6")

servo_ID= servo.ListServos



def val_map(value , in_min , in_max, out_min , out_max ): 
    if ((in_min <= value <= in_max) or (in_min >= value >= in_max) ):
          out = ((value-in_min)*((out_max-out_min)/(in_max-in_min)))+out_min 
          return out
    else :
        return "The input value should be in [in_min , in_max]"
        return 0
    
while True :
    val = float(input("entrez la valeur a mapper : "))
    print (val_map(val,360,0,servo_min,servo_max))


# while True :
#     angle = int (input ("give an angle : "))
#     servo.WritePosition(4, angle)
#     print("task Done ...")