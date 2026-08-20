import math

while True :

    x , z = float (input ("entrez la valeur de de X : ")) , float (input ("entrez la valeur de de Z : "))

    a = 110
    b = 100
    r = math.sqrt((x**2)+(z**2))

    if (abs(a-b) <= r <= a+b ) :
        Theta_2 = math.acos((((a**2)+(b**2))-(r**2))/(2*a*b))
        Theta_1 =  math.acos((((b**2)+(r**2)-(a**2))/(2*b*r))) - math.atan2(z , x)
#(math.pi) +
        Theta_2 = math.degrees(Theta_2)
        Theta_1 = math.degrees(Theta_1) % 360 # to normalize the angle (0 < theta_2 < 360)

        print("valeur de Theta_1 : " , Theta_1)
        print("valeur de Theta_2 : " , Theta_2)

    else : 
        print ("Target out of reach")