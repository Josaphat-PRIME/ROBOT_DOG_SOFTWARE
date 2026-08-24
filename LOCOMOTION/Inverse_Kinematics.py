import math

# variables and legs parameters
lower_leg = 110
upper_leg = 100

a = 30
b = 100
c = 20
d = upper_leg

k1 = d / a
k2 = d / c
k3 = ( (d**2)+(a**2)-(b**2)+(c**2) )/(2*c*a)

def angles(x,z) : 

    # x , z = float (input ("entrez la valeur de de X : ")) , float (input ("entrez la valeur de de Z : "))

    r = math.sqrt((x**2)+(z**2))

    if (abs(lower_leg-upper_leg) <= r <= lower_leg+upper_leg ) :
        Theta_2 = math.acos((((lower_leg**2)+(upper_leg**2))-(r**2))/(2*lower_leg*upper_leg))
        Theta_1 =  math.acos((((upper_leg**2)+(r**2)-(lower_leg**2))/(2*upper_leg*r))) + math.atan2(x , z) - (math.pi/2)
    #(math.pi) +

    # Four-barlinkage conversion
        A = k2 + math.cos(Theta_2)
        B = math.sin(Theta_2)
        C = k3 + k1*math.cos(Theta_2)
        R = math.sqrt((A**2)+(B**2))
        phi = math.atan2(B,A) 
        Theta_e = abs(phi + math.acos(C/R))
        #end of the four bars linkages conversion
        Theta_e = math.degrees(Theta_e)
        Theta_2 = math.degrees(Theta_2)
        Theta_1 = math.degrees(Theta_1) % 360 # to normalize the angle (0 < theta_2 < 360)
        

        # print("valeur de Theta_e : " , Theta_e)
        # print("valeur de Theta_1 : " , Theta_1)
        # print("valeur de Theta_2 : " , Theta_2)

        return Theta_1 , Theta_e
    else : 
        print ("Target out of reach")


