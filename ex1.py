i = 0
a = int(input("donné le 1er coté: "))
print(a)
b = int(input("donné le 2eme coté: "))
print(b)
c =int(input("donné le 3eme coté: "))
print(c)
d: int = a*b
e: int = a*c
if d == e :
    print("vrai")
elif d != e :
    print("faux")

else :
    print("faux")
