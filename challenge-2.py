

from posixpath import split

# first step: take input from user
ip = input("enter your ip here")
oct1, oct2, oct3, octk = ip.split(".")
oct4, oct5 = octk.split("/")
oct1 = int(oct1)
oct2 = int(oct2)
oct3 = int(oct3)
oct4 = int(oct4)
oct5 = int(oct5)

# second step: check if the input in range
if oct1 < 0 or oct1 > 255:
    print("error oct1 not in range")
if oct2 < 0 or oct2 > 255:
    print("error oct2 not in range")
if oct3 < 0 or oct3 > 255:
    print("error oct3 not in range")
if oct4 < 0 or oct4 > 255:
    print("error oct4 not in range")
if oct5 != 8 or oct5 != 16 :#or oct5 != 24 or oct5 != 32:
    print("error oct5 not in range")

print(oct5)
