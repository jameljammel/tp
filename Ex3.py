import math

a = int(input("donné a:"))
b = int(input("donné b:"))
c = int(input("donné c:"))
def denifi_triangle(a,b,c):
    d: int = (a+b+c)/2
    print(d)
    if a >= d and b >= d and c >= d :

        r: bool = "true"
        print(r)

    elif a < d and b > d and c > d :
        r: bool = "false"
        print(r)
    else:
        print("false")

print(denifi_triangle(a,b,c))


