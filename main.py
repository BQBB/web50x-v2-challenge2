def checka(y,y1):
    if y == 10:
        print("Class:A, Designation: Private")
    elif y==127 and y1 in range(1,256):
         print("Class:A, Designation: Special")
    else:
        print("Class:A, Designation: Public")  

def checkb(y,y1):
    if y == 172 and y1 in range(16,32):
        print("Class:B, Designation: Private")
    else:
        print("Class:B, Designation: Public") 

def checkc(y,y1):
    if y == 192 and y1 ==168:
        print("Class:C, Designation: Private")
    else:
        print("Class:C, Designation: Public") 

x=input("Enter your IP:")
o=x.split(".")

class address:
    def __init__(self,oct1,oct2,oct3,oct4):
        self.oct1=oct1
        self.oct2=oct2
        self.oct3=oct3
        self.oct4=oct4
        
p1=address(o[0],o[1],o[2],o[3])
x1=int(p1.oct1)
x2=int(p1.oct2)
x3=int(p1.oct3)
x4=int(p1.oct4)
if x1 in range(1,128):
    checka(x1,x2)
elif x1 in range(128,192):
    checkb(x1,x2)
elif x1 in range(192,224):
    checkc(x1,x2)
elif x1 in range(224,240):
    print("Class:D, Designation: Special")   
elif x1 in range(240,256):
    print("Class:E, Designation: Special") 
else:
    print("Invalid IP")        