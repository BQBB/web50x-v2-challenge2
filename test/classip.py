
ipaddr=input("enter address: ")
ip=ipaddr.split("/")
mask=int(ip[1])
addr=ip[0]
x=addr.split(".")
y = []
for element in x:
    y.append(int(element))


if mask in range(1,33):
    if y[0] in range(0,127):
        if y[0]==10:
            print("class A ,private")
        elif  y[0]==127:
            print("class A , special")  
        else:
            print("class A , public")
    elif y[0] in range(128,191):
        if y[0]==172 and y[1] in range(16,31):
            print("class B , private")       
        else :
            print("class B public")    
    elif y[0] in range(192,223):
        if y[0]==192 and y[1]==168:
            print("class c , private")       
        else :
            print("class B public") 
    elif y[0] in range(224,239):
            print("class D , special")       
    else :
         print("class E special")    
else:
    print("out of range")                     