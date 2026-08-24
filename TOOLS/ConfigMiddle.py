### Before start make shure that only one servo is connected to the servo driver and make shure to choose the right port

from st3215 import ST3215
import time

servo = ST3215("COM6")

print("--------------------------------- ")

servo_ID = int (input ("Choose your servo ID : "))

print("Checking current servo value ... ")

old_value = servo.ReadPosition(servo_ID)

print("--------------------------------- ")


print("Current servo value is : " , old_value )

print("Setting middle ... ")

servo.UnLockEprom(servo_ID)

servo.DefineMiddle(servo_ID)

servo.LockEprom(servo_ID)
time.sleep(1)
new_value = servo.ReadPosition(servo_ID)

print("The new servo value is : " ,  new_value )

print("--------------------------------- ")

if (new_value == 2048) :
    print ("Task succesfully completed ")
else : 
    print("Task failed : please do not move the robot arm when setting the middle or make shure it stable")

print("--------------------------------- ")
