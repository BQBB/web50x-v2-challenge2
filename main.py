# ----------------------------------------------------------------
# stage 1
# ----------------------------------------------------------------
# input the ip
ip = input("input the IP address")

# spilt the ip by / and save the mask in new variable (ipMask) 
ipMaskSpilt = ip.split('/')
ipMask = ipMaskSpilt[1]
# change Mask data type to int 
ipMask = int(ipMask)

# take the ip before the slash and split it by . 
Ip = ipMaskSpilt[0].split('.')
#  change the Ip list items to intger 
for index in range(len(Ip)):
    Ip[index] = int(Ip[index]) 
   
# ----------------------------------------------------------------
# stage 2
# ----------------------------------------------------------------
# checking the ip address and checking mask 
for index in range(len(Ip)):
    # ipcheker[index] = int(ip[index])
    if Ip[index] > 255: raise ValueError("Invalid IP address")
    elif Ip[index] < 0: raise ValueError("Invalid IP address")
    if index > 3 : raise ValueError("Invalid IP address")
    
# checking the Mask if not valied
if ipMask > 32: raise ValueError("Invalid IP mask")
elif ipMask < 0: raise ValueError("Invalid IP mask")


# ----------------------------------------------------------------
# stage 3
# ----------------------------------------------------------------
# check the class 
# ----------------------------------------------------------------
#                 class A
#   puplic 
if Ip[0] >= 1 and Ip[0] <= 127 and Ip[1] == 0 and Ip[2] == 0 and Ip[3] == 0: 
    print("class is A, Designation is public")
    
#   private
if Ip[0] >= 1 and Ip[0] <= 127: 
    if Ip[0] == 10 :
        if Ip[1] >= 0 and Ip[1] <= 255:
            if Ip[2] >= 0 and Ip[2] <= 255:
                if Ip[3] >= 0 and Ip[3] <= 255:
                     print("class is A,Designation is private")
                     
#  Special         
if Ip[0] == 127 :
    if Ip[1] >= 0 and Ip[1] <= 255:
        if Ip[2] >= 0 and Ip[2] <= 255:
            if Ip[3] >= 1 and Ip[3] <= 255:
                print("class is A,Designation is special")
                print("---  loopback class ---")                  
# ----------------------------------------------------------------
#                 class B
#   public
if Ip[0] >= 128 and Ip[0] <= 191 : 
    if Ip[1] >= 0 and Ip[1] <= 255 :
        print("class is B, Designation is public")
    
#  private 
if Ip[0] >= 128 and Ip[0] <= 191 :   
    if Ip[0] == 172:
        if Ip[1] >= 16 and Ip[1] <= 31:
            if Ip[2] >= 0 and Ip[2] <= 255 :
                if Ip[3] >= 0 and Ip[3] <= 255 :
                     print("class is B, Designation is Private")
# ----------------------------------------------------------------
#                 class c
#   public       
if Ip[0] >= 192 and Ip[0] <= 223 :
    if Ip[1] >= 0 and Ip[1] <= 255 :
        if Ip[2] >= 0 and Ip[2] <= 255 :
            if Ip[3] == 0 :
                print("class is C, Designation is public")
#  private 
if Ip[0] == 192  :
    if Ip[1] == 168:
        if Ip[2] >= 0 and Ip[2] <= 255 :
            if Ip[3] >= 0 and Ip[3] <= 255:
                 print("class is C,Designation is private")

# ----------------------------------------------------------------
#                 class D
#   public    
if Ip[0] >= 224 and Ip[0] <= 239 : 
    print("class is D, Designation is public")
    
# ----------------------------------------------------------------
#                 class E
#   public       
if Ip[0] >= 240 and Ip[0] <= 255:
    print("class is E, Designation is public")
   