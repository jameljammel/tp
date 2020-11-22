# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

i = 0
a = input("donné le 1er coté: ")
print(a)
b = input("donné le 2eme coté: ")
print(b)
c = input("donné le 3eme coté: ")
print(c)
d = a*b
e = a*c
while c < 20 :
  if d == e :
    print("vrai")
