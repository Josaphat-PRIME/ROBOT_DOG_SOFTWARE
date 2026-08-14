### Before start make shure that only one servo is connected to the servo driver 

from st3215 import ST3215

servo = ST3215("/dev/ttyAMA3")  # make shure to choose the right UART port

print("Starting ...")

old_ID= servo.ListServos()

print("Current ID is : ",old_ID[0])

New_ID = int(input("Type the new ID and press ENTER "))

if (0< New_ID < 254) :
    print("Changing ID ..." )
    servo.ChangeId(old_ID[0], New_ID)
    current_ID= servo.ListServos()
    print("Checking update ..." )
    if (current_ID[0] == New_ID):
        print("the new_ID is : " ,  New_ID )
        print( "Task Done ")

    else :
        print("Error occured, chech your wiring or your UART port")

else : 
    print("Your ID must be in range of 1-254 ")