n = int(input("enter n : "))

def fibonnaci (n) :
  
    a = 0
    b = 1  
    liste =[]
    while a < n :
        print(a) 
        liste.append(a)
        a , b = b , b+a

    print(liste[::3])

fibonnaci(n)
