

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
# if oct5 != 8  or  oct5 != 16  or  oct5 !=  24  or  oct5 != 32:
if oct5 == 8 or oct5 == 16 or oct5 == 24 or oct5 == 32:
    print()
else:
    print("error oct5 not in range")

# section for checking classes
if oct1 <= 127:
    # print("calss A")
    ip_class = "A"
elif oct1 >= 128 and oct1 <= 191:
    # print("class B")
    ip_class = "B"
elif oct1 >= 192 and oct1 <= 223:
    # print("class C")
    ip_class = "C"
elif oct1 >= 224 and oct1 <= 239:
    # print("class D")
    ip_class = "D"
elif oct1 >= 240 and oct1 <= 255:
    # print("class E")
    ip_class = "E"


# designation section
if ip_class == "A":
    if oct1 == 127 and oct4 > 0:
        ip_designation = "special"
    elif oct1 == 10:
        ip_designation = "private"
    else:
        ip_designation = "public"
if ip_class == "B":
    if oct1 == 169 and oct2 == 254:
        ip_designation = "automatic-private"
    elif oct1 == 172 and (oct2 >= 16 and oct2 <= 31):
        ip_designation = "private"
    else:
        ip_designation = "public"
if ip_class == "C":
    if oct1 == 192 and oct2 == 168:
        ip_designation = "private"
    else:
        ip_designation = "public"

if ip_class == "D":
    ip_designation = "multicasting"

if ip_class == "E":
    ip_designation = "multicasting"


print(f"class:{ip_class}, Designation:{ip_designation} ")
