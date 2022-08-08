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
# class range definition
classA = range(1,128)
classB = range(128,192)
classC = range(192,224)
classE = range(224,240)
classD = range(240,256)

# ----------------------------------------------------------------
# stage 3
# ----------------------------------------------------------------
# check the class 
# ----------------------------------------------------------------
typeOfClass = ""
if Ip[0] in classA:
    typeOfClass = "A"
elif Ip[0] in classB:
    typeOfClass = "B"
elif Ip[0] in classC:
    typeOfClass = "C"
elif Ip[0] in classD:
    typeOfClass = "D"
elif Ip[0] in classE:
    typeOfClass = "E"   
    
# ----------------------------------------------------------------
# stage 4
# ----------------------------------------------------------------
# check the Designation
# ----------------------------------------------------------------
if typeOfClass == "A" and Ip[0] == 10:  #good
    designationType = "private"
elif typeOfClass == "A" and Ip[0] == 127:
   designationType = "special"
elif typeOfClass == "A" and Ip[0] >= 1:  #good
    designationType = "public"
elif typeOfClass == "B" and Ip[0] == 172 and Ip[1]  >= 16 and Ip[1] <= 32: #good
    designationType = "private"
elif typeOfClass == "B" :     #good
    designationType = "public"
elif typeOfClass == "C" and Ip[0] == 192 and Ip[1] == 168:  #good
    designationType = "Private"
elif typeOfClass == "C" and Ip[0] != 192:   #good
    designationType = "public"
elif typeOfClass == "D":
    designationType = "public"
elif typeOfClass == "E":
    designationType = "public"
else:
    designationType = "public"
# ----------------------------------------------------------------
# stage 5
# ----------------------------------------------------------------
# print
# ----------------------------------------------------------------
print(f"the class is {typeOfClass} and the designation is {designationType}")    

