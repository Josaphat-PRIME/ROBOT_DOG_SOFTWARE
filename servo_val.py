from st3215 import ST3215
servo = ST3215("COM6")


while True :
    a= int(input("vvaleur a anguler : "))
    servo.MoveTo(3 , a)

# servo.StopServo(3)

# while True :
#     a = servo.ReadPosition(3)
#     print (a)