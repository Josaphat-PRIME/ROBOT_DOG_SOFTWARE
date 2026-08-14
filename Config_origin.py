from st3215 import ST3215

servo = ST3215("/dev/ttyAMA3")
valeur =servo.ReadPosition(2)
servo.WritePosition(2,valeur)
servo_ID= int (input ("Choose your servo ID: "))


min_pos , max_pos =servo.TareServo(servo_ID)

# S= servo.getBlockPosition(servo_ID)
# print(S)
# servo.StopServo(servo_ID)