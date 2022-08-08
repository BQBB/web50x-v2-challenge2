def validatingIP(ip, octets, subMask):
    
    
    if len(octets) != 4:
        print(f"IP address {ip} is not valid.")
        return False
    for octet in octets:
        if not isinstance(octet, int):
            print(f"IP address {ip} is not valid.")
            return False
        if octet < 0 or octet > 255:
            print(f"IP address {ip} is not valid.")
            return False
    if subMask < 0 or subMask > 31:
        print(f"The subnet mask {subMask} is not valid.")
        return False
    
    return True


def findingClass(octets):

    if octets[0] > 0 and octets[0] <= 126:
        return "A"
    
    elif octets[0] >= 128 and octets[0] <= 191:
        return "B"
   
    elif octets[0] >= 192 and octets[0] <= 223:
        return "C"

    elif octets[0] == 127:
        return "C"
   
    elif octets[0] >= 224 and octets[0] <= 239:
        return "D"
   
    else:
        return "E"


def findingDesignation(octets, IPClass):
    if IPClass == "A":
        if octets[0] == 10:
            return "Private"
        else:
            return "Public"
    elif IPClass == "B":
        if octets[0] == 172 and octets[1] >= 16 and octets[1] <= 31:
            return "Private"
        else:
            return "Public"
    elif IPClass == "C":
        if octets[0] == 192 and octets[1] == 168:
            return "Private"
        elif octets[0] == 127:
            return "Special"
        else:
            return "Public"
    else:
        return "Special"


