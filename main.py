def solution():
    pass


if __name__ == '__main__':
    pass


    
userIP = input("input your IP : ")
ip, mask = userIP.split('/')
octet = ip.split('.')
octet_mask = octet + [mask]


#for index in len(octet) : int(octet[index])

for i in range(0, len(octet_mask)):
    octet_mask[i] = int(octet_mask[i])



if (int(mask) in range(0,33)) :

    if len(octet_mask[:-1]) == 4 : 

        for ip in octet :
            if (int(ip) in range(0,256)) :    

                if octet_mask[0] in range(0,128) :
                    if octet_mask[0] == 10 :
                        print("class : A , Designation : private")
                        exit(1)

                    elif octet_mask[0] == 127 :
                        print("class : A , Designation : special")
                        exit(1)

                    else :
                        print("class : A , desibnation : puplic") 
                        exit(1)  




                if octet_mask[0] in range(128,192) :
                    if octet_mask[0] == 172 :
                        print("class : B , Designation : private")
                        exit(1)


                    else :
                        print("class : B , desibnation : puplic")  
                        exit(1) 


                if octet_mask[0] in range(192,224) :
                    if octet_mask[0] == 192 :
                        print("class : C , Designation : private")
                        exit(1)


                    else :
                        print("class : C , desibnation : puplic")
                        exit(1)   


                if octet_mask[0] in range(224,240) :

                    print("class : D , desibnation : special ")
                    exit(1)  


                if octet_mask[0] in range(240,255) :
                
                        print("class : E , desibnation : special ")     
            
            
            else :
                print("octet range must be from 0 to 255")
                  
    else :
        print("octets must be 4 number")
else :
    print("mask range must be from 0 to 32")        