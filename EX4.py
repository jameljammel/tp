import math
from math import sqrt

a = int(input("donner a:"))

b= int(input("donner b:"))


def nb_triangle_speciaux(a,b) :
    i = 1
    while i > a and i < b :
        c = i
        i +=1
        print(c)
        P: int = (a*b) + (b*c) + (a*c)
        k: float = ((pow(a,2) - pow(b,2) - pow(c,2))/(2*a))
        g: float = pow(k,2)
        h: float = sqrt((pow(c,2)) - g)
        if P == h :
            print("nombre de triangle :", c)
            
        else:
            print("pas de triangle")

