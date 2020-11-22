import math
from math import sqrt



a = int(input("entrer a:"))
b = int(input("entrer b:"))
c = int(input("entrer c:"))
def air_donne(u1,u2,u3):
    A = (1 / 2 * (math.sqrt((pow(u1, 2) * (pow(u2, 2)) - (pow((u1 - u2 - u3), 2) / 2)))))
    print(A)

if a > b and b > c:
    print("c est le minimum des trois valeurs")
    u1: int = pow(c,2)
    print(u1)
    u2: int = pow(b,2)
    print(u2)
    u3: int = pow(a,2)
    print(u3)

elif a < b and b > c :
    u1: int = pow(a,2)
    print(u1)
    u2: int = pow(c,2)
    print(u2)
    u3: int = pow(b,2)
    print(u3)

elif a < b and b < c:
    print("a est la plus peite valeur")
    u1: int = pow(a,2)
    print(u1)
    u2: int = pow(b,2)
    print(u2)
    u3: int = pow(c,2)
    print(u3)

else :
    print("erruer")


print(air_donne(u1,u2,u3))

