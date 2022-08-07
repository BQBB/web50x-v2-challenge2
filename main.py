def solution():

    # Params
    classes = {
        'a': {
            'public': [range(1, 127), range(0, 256), range(0, 256), range(1, 255)],
            'private': [range(10, 11), range(0, 256), range(0, 256), range(0, 256)],
            'special': [range(127, 128), range(0, 256), range(0, 256), range(1, 256)]
        },
        'b': {
            'public': [range(128, 192), range(1, 256), range(0, 256), range(1, 255)],
            'private': [range(172, 173), range(16, 32), range(0, 256), range(0, 256)],
            'special': None
        },
        'c': {
            'public': [range(192, 224), range(0, 256), range(1, 255), range(1, 255)],
            'private': [range(192, 193), range(168, 169), range(0, 256), range(0, 256)],
            'special': None
        },
        'd': {
            'public': [range(224, 240), range(0, 256), range(0, 256), range(0, 256)],
            'private': None,
            'special': None
        },
        'e': {
            'public': [range(240, 255), range(0, 256), range(0, 256), range(0, 255)],
            'private': None,
            'special': None
        }
    }

    output = {}

    # User Input
    print('Please enter an ip in this format x.x.x.x/x: ')
    user_input = input()

    # Format Validation
    if not ("/" in user_input) or "-" in user_input:
        raise Exception("The IP in this format x.x.x.x/x")

    # Input Splitting
    data = user_input.split("/")

    subnet_bits = int(data[1])

    # IP octets
    ip = data[0]
    octets = ip.split(".")
    first_octet = int(octets[0])
    second_octet = int(octets[1])
    third_octet = int(octets[2])
    fourth_octet = int(octets[3])

    # Value Validation
    accepted_ranges = [range(0, 256), range(1, 33)]
    if not (first_octet in accepted_ranges[0]) or not (second_octet in accepted_ranges[0]) or not (
            third_octet in accepted_ranges[0]) or not (fourth_octet in accepted_ranges[0]):
        raise Exception("IP Octets should be between 0 and 255")

    if not (subnet_bits in accepted_ranges[1]):
        raise Exception("Subnet bits should be between 1 and 32")

    # Classification

    # Private A
    if (first_octet in classes['a']['private'][0]) and (
            second_octet in classes['a']['private'][1]) and (
            third_octet in classes['a']['private'][2]) and (
            fourth_octet in classes['a']['private'][3]):
        output['class'] = 'A'
        output['designation'] = 'Private'

    # Public A
    elif (first_octet in classes['a']['public'][0]) and (
            second_octet in classes['a']['public'][1]) and (
            third_octet in classes['a']['public'][2]) and (
            fourth_octet in classes['a']['public'][3]):
        output['class'] = 'A'
        output['designation'] = 'Public'

    # Special A
    elif (first_octet in classes['a']['special'][0]) and (
            second_octet in classes['a']['special'][1]) and (
            third_octet in classes['a']['special'][2]) and (
            fourth_octet in classes['a']['special'][3]):
        output['class'] = 'A'
        output['designation'] = 'Public'

    # Public B
    elif (first_octet in classes['b']['public'][0]) and (
            second_octet in classes['b']['public'][1]) and (
            third_octet in classes['b']['public'][2]) and (
            fourth_octet in classes['b']['public'][3]):
        output['class'] = 'B'
        output['designation'] = 'Public'

    # Private B
    elif (first_octet in classes['b']['private'][0]) and (
            second_octet in classes['b']['private'][1]) and (
            third_octet in classes['b']['private'][2]) and (
            fourth_octet in classes['b']['private'][3]):
        output['class'] = 'B'
        output['designation'] = 'Private'

    # Private C
    elif(first_octet in classes['c']['private'][0]) and (
            second_octet in classes['c']['private'][1]) and (
            third_octet in classes['c']['private'][2]) and (
            fourth_octet in classes['c']['private'][3]):
        output['class'] = 'C'
        output['designation'] = 'Private'

    # Public C
    elif (first_octet in classes['c']['public'][0]) and (
            second_octet in classes['c']['public'][1]) and (
            third_octet in classes['c']['public'][2]) and (
            fourth_octet in classes['c']['public'][3]):
        output['class'] = 'C'
        output['designation'] = 'Public'

    # Class D
    elif (first_octet in classes['d']['public'][0]) and (
            second_octet in classes['d']['public'][1]) and (
            third_octet in classes['d']['public'][2]) and (
            fourth_octet in classes['d']['public'][3]):
        output['class'] = 'D'
        output['designation'] = 'Public'

    # Class E
    elif (first_octet in classes['e']['public'][0]) and (
            second_octet in classes['e']['public'][1]) and (
            third_octet in classes['e']['public'][2]) and (
            fourth_octet in classes['e']['public'][3]):
        output['class'] = 'E'
        output['designation'] = 'Public'

    return output
    pass


if __name__ == '__main__':
    out = solution()
    print(f'Output: Class: {out["class"]}, Designation: {out["designation"]}')

    pass
