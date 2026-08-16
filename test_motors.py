from st3215 import ST3215
servo_min = 0
servo_max = 4095


servo = ST3215("/dev/ttyAMA3")

servo_ID= servo.ListServos

def map(x , in_min , in_max, out_min , out_max ):

    out = ((x-in_min)*((out_max-out_min)/(in_max-in_min)))+out_min

    return out
while True :
    val = float(input("entrez la valeur a mapper : "))
    print (map(val,360,0,servo_min,servo_max))


# while True :
#     angle = int (input ("give an angle : "))
#     servo.WritePosition(4, angle)
#     print("task Done ...")