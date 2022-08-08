#variables
z = input("Enter IP Address as like x.x.x.x/x : ")
y = z.split("/")
x = y[0].split(".")
y[1] = int(y[1])
for i in range(len(x)):
    x[i] = int(x[i])
v = 1
#functions
def ClassA(n1,n2):
    if n1 == 10:
        print("Class:A, Designation: Private")
    elif n1==127 and n2 in range(1,256):
         print("Class:A, Designation: Special")
    else:
        print("Class:A, Designation: Public")  

def ClassB(n1,n2):
    if n1 == 172 and n2 in range(16,32):
        print("Class:B, Designation: Private")
    else:
        print("Class:B, Designation: Public") 
        
def ClassC(n1,n2):
    if n1 == 192 and n2 ==168:
        print("Class:C, Designation: Private")
    else:
        print("Class:C, Designation: Public") 
#main code
for n in x:
    if n < 0 or n > 255:
        v = 2
if y[1] < 0 or y[1] > 32:
    v = 3
if len(x) != 4:
    v = 4
if v == 2:
    print("Invalid octal, must be between 0-255")
elif v == 3:
    print("Invalid mask, must be between 0-32")
elif v == 4:
    print("Wrong IP, must write 4 octal")
else:
    if x[0] in range(1,128):
        ClassA(x[0],x[1])
    elif x[0] in range(128,192):
        ClassB(x[0],x[1])
    elif x[0] in range(192,224):
        ClassC(x[0],x[1])
    elif x[0] in range(224,240):
        print("Class:D, Designation: Special")   
    elif x[0] in range(240,256):
        print("Class:E, Designation: Special")
    elif x[0] == 0:
        print("Invalid IP Address")       
