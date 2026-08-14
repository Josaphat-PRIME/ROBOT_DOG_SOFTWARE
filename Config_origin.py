from st3215 import ST3215

servo = ST3215("/dev/ttyAMA3")

servo_ID= int (input ("Choose your servo ID: "))
print("This actual position is : ", servo.ReadPosition(servo_ID))
while True :
    print(servo.ReadStatus(servo_ID))
    angle = int (input ("give an angle : "))
    servo.WritePosition(servo_ID, angle)
    print("task Done ...")