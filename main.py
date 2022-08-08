def validate_ip_address(address):
    parts = address.split(".")

    if len(parts) != 4:
        print("IP address {} is not valid".format(address))
        return False

    for part in parts:
        if not isinstance(int(part), int):
            print("IP address {} is not valid".format(address))
            return False

        if int(part) < 0 or int(part) > 255:
            print("IP address {} is not valid".format(address))
            return False
 
    
    return parts


def check(value):
        try:

            h = [int(item) for item in value] 

            if h[0] == 127:
                print("Class: A , Designation: Special")
            elif 0 <= h[0] <= 127 and h[1] == 10:
                    print("Class: A , Designation: private")
            elif 0 <= h[0] <= 127 and h[1] != 10:
                    print("Class: A , Designation: public")
            elif 128 <= h[0] <= 191 and  16 <= h[1] <= 31:
                    print("Class: B , Designation: private")
            elif 128 <= h[0] <= 191 and  h[1] != privateB:
                    print("Class: B , Designation: public")
            elif 192 <= h[0] <= 223 and h[1] == 168:
                    print("Class: C , Designation: private")
            elif 192 <= h[0] <= 223 and h[1] != 168:
                    print("Class: C , Designation: public")
            elif 224 <= h[0] <= 239:
                    print("Class: D , Designation: Special")  
            elif 240 <= h[0] <= 255:
                    print("Class: E , Designation: Special") 
            else:
                print("Please enter a valid IP address !")

        except TypeError:
                return False



privateB = range(16,31)
IP = input("type your IP : ")
myIP = validate_ip_address(IP)
s = check(myIP)