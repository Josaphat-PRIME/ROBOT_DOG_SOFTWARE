from st3215 import ST3215
servo = ST3215("COM6")



a= int(input("valeur a anguler : "))
servo.MoveTo(3, a)
b = servo.ReadPosition(3)
print (b)
# servo.StopServo(3)

# while True :
#     
#     