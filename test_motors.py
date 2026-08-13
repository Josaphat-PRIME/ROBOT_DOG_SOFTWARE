from st3215 import ST3215

servo = ST3215("/dev/ttyAMA3")

servo_ID= int (input ("Choose your servo ID: "))

while True :
    angle = int (input ("give an angle : "))
    servo.WritePosition(servo_ID, angle)
    print("task Done ...")