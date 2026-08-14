from st3215 import ST3215

servo = ST3215("/dev/ttyAMA3")

servo_ID= servo.ListServos

while True :
    angle = int (input ("give an angle : "))
    servo.WritePosition(3, angle)
    print("task Done ...")