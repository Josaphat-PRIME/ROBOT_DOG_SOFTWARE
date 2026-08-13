from st3215 import ST3215

servo = ST3215("/dev/ttyAMA3")
while True :
    print("give an angle : .. ")
    a = int (input ())
    servo.WritePosition(2, a)
    print("task Done ...")