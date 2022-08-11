

def ipclasses(IPAddress):

    if(len(octets) == 4):
        if(Musk in range(0,33)):
            if (int(octets[0]) in range(0,256) and int(octets[1]) in range(0,256) and int(octets[2]) in range(0,256) and int(octets[3]) in range(0,256)):


                        if(IPAddress[0] >= 0 and IPAddress[0] <= 9):
                            return "Class A , Designation: Public"

                        elif(IPAddress[0] == 10 and IPAddress[1] in range(0, 256)):
                            return "Class A , Designation: Private"

                        elif(IPAddress[0] >= 11 and IPAddress[0] <= 126):
                            return "Class A , Designation: Public"

                        elif(IPAddress[0] == 127 and IPAddress[1] in range(0,256)):
                            return "Class A , Designation: Special"

                        elif(IPAddress[0] in range(128, 172) and IPAddress[1] in range(0, 256)):
                            return "Class B , Designation: Public"

                        elif(IPAddress[0] == 172 and IPAddress[1] in range(0, 16)):
                            return "Class B , Designation: Public"

                        elif(IPAddress[0] == 172 and IPAddress[1] in range(16, 32)):
                            return "Class B , Designation: Private"

                        elif(IPAddress[0] == 172 and IPAddress[1] in range(32, 256)):
                            return "Class B , Designation: Public"

                        elif(IPAddress[0] in range(173,192) and IPAddress[1] in range(0, 256)):
                            return "Class B , Designation: Public"

                        elif(IPAddress[0] == 192 and IPAddress[1] in range(0, 168)):
                            return "Class C , Designation: Public"

                        elif(IPAddress[0] == 192 and IPAddress[1] in range(168, 256)):
                            return "Class C , Designation: Private"

                        elif(IPAddress[0] in range(193,224) and IPAddress[1] in range(0, 256)):
                            return "Class C , Designation: Public"

                        elif(IPAddress[0] >= 224 and IPAddress[0] <= 239):
                            return "Class D, Reserved for multicast groups."

                        else:
                            return "Class E,  Reserved for future use, or Research & Development Purposes."
            else:
                print(" octet of IP must be in range (0-255)")                    
        else:
            print(" Musk must be in range (0-32)")        

    else:
        print("The IPAdress Most be in Format: x.x.x.x/x")            

if __name__ == "__main__":

    IP_mask = input("Enter your ip address :")          #IP as 192.168.0.1/24
    IP_mask_s = IP_mask.split('/')                      #IP as [192.168.0.1,24]
    IPAddress = (IP_mask_s[0])                          #IP as 192.168.0.1
    Musk = int(IP_mask_s[1])                            #Musk of IP 24
    octets = IPAddress.split('.')                       #octets as 192,168,0,1
    octets = [int(i) for i in octets]


networkClass = ipclasses(octets)
print("Output :",networkClass)

