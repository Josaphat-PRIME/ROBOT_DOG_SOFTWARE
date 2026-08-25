from st3215 import ST3215
servo = ST3215("COM6")


while True :
    a= int(input("valeur a anguler : "))
    a  = 2048 + ((a-180)*(26/15)*(4095/360))
    servo.MoveTo(3, int(a))
    b = servo.ReadPosition(3)
    print (a)
# servo.StopServo(3)

# 
#     
#     