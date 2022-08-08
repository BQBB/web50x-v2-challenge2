def solution():
    print('Enter IP :')
    x = input()

    if not ("/" in x) or "-" in x:
        raise Exception("The IP format Should be (x.x.x.x/x)")

    parts = x.split("/")

    mask = int(parts[1])
    octets = parts[0].split(".")

    if not (mask in range(1, 33)):
        raise Exception("Mask should be in range (1-33)")

    for i in range(0, 4):
        octets[i] = int(octets[i])

    for i, octet in enumerate(octets):
        if i == 3 and not (octet in range(1, 255)):
            raise Exception("octets should be in range (1-254)")
        elif not (octet in range(0, 256)):
            raise Exception("octets should be in range (0-255)")

    if octets[0] in range(10, 11):
        print("Class A, Designation Private")
    elif octets[0] in range(127, 128):
        print("Class A, Designation special")
    elif octets[0] in range(1, 126):
        print("Class A, Designation public")
    elif octets[0] in range(172, 173):
        print("Class B, Designation private")
    elif octets[0] in range(128, 192):
        print("Class B, Designation public")
    elif octets[0] in range(192, 193):
        print("Class C, Designation private")
    elif octets[0] in range(192, 224):
        print("Class C, Designation special")
    elif octets[0] in range(224, 240):
        print("Class D, Designation private")
    elif octets[0] in range(240, 255):
        print("Class E, Designation private")


if __name__ == '__main__':
    solution()
