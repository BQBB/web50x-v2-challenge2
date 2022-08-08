from fun import validatingIP
from fun import findingClass
from fun import findingDesignation
programWorking = True

while programWorking: 

    givenIP = input("Enter the ip 'format: x.x.x.x/x' or enter 'exit' to quit: ")
    if givenIP == "exit":
        programWorking == False
        print("Thank you! exiting now...")
        exit()
    if '/' not in givenIP:
        print("Format error! please enter the subnet mask, format: x.x.x.x/x")
        continue
    octets = givenIP.split(".")
    lastE = octets.pop()
    theSlash = lastE.split("/")
    octets.append(theSlash[0])
    subMask = int(theSlash[1]) # I know splitting was a mess, sorry :(
    octets = [int(i) for i in octets]
    if not validatingIP(givenIP, octets, subMask):
        continue
    networkClass = findingClass(octets)
    networkDesignation = findingDesignation(octets, networkClass)
    print(f"Class: {networkClass}, Designation: {networkDesignation}")



if __name__ == '__main__':
    pass