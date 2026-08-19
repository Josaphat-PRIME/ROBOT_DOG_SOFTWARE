from st3215 import ST3215

servo = ST3215("COM6")

servo_ID= int (input ("Choose your servo ID: "))

print("Checking current servo value ... ")

value = servo.ReadPosition(servo_ID)

print("current servo value is" , value )

servo.DefineMiddle(servo_ID)
#min_pos , max_pos =servo.TareServo(servo_ID)
value = servo.ReadPosition(servo_ID)
print("The new servo value is : " ,  value )

# S= servo.getBlockPosition(servo_ID)
# print(S)
# servo.StopServo(servo_ID)