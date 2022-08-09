class IpAddress:
    def __init__(self, octets, mask):
        self.ip_class = None
        self.designation = None

        self.octets = octets
        self.mask = mask
        self.classify()

    @classmethod
    def from_string(cls, input):
        result = cls.__validate_format(input)
        if result['error_message'] != "Success":
            raise Exception(result['error_message'])

        result = cls.__validate_value(input)
        if result['error_message'] != "Success":
            raise Exception(result['error_message'])

        return cls(result['octets'], result['subnet_mask'])


    @classmethod
    def __validate_format(cls, input) -> dict:
        result = { "error_message": "Success" }

        if not ("/" in input) or "-" in input:
             result["error_message"] = "The IP in this format x.x.x.x/x"
        return result

    @classmethod
    def __validate_value(cls, input) -> dict:
        result = { "error_message": "Success" }

        ip, subnet_mask = input.split("/")
        octets = ip.split(".")

        accepted_ranges = [range(0, 256), range(1, 255), range(1, 33)]

        subnet_mask = int(subnet_mask)
        for i, octet in enumerate(octets):
            octet = int(octet)

            if i == 3 and not(octet in accepted_ranges[1]):
                result['error_message'] = "Last IP Octet should be between 1 and 254"
                return result
            elif not(octet in accepted_ranges[0]):
                result['error_message'] = "IP Octets should be between 0 and 255"
                return result

            octets[i] = octet

        if not (subnet_mask in accepted_ranges[2]):
            result["error_message"] = "Subnet bits should be between 1 and 32"

        result["octets"] = octets
        result["subnet_mask"] = subnet_mask

        return result

    def classify(self):
        classes = {
            'a': {
                'public': range(1, 127),
                'private': range(10, 11),
                'special': range(127, 128)
            },
            'b': {
                'public': range(128, 192),
                'private': [range(172, 173), range(16, 32)],
            },
            'c': {
                'public': range(192, 224),
                'private': range(192, 193),
            },
            'd': {
                'private': range(224, 240),
            },
            'e': {
                'private': range(240, 255),
            }
        }

        # Private A
        if self.octets[0] in classes['a']['private']:
            self.ip_class = 'A'
            self.designation = 'Private'

        # Public A
        elif self.octets[0] in classes['a']['public']:
            self.ip_class = 'A'
            self.designation = 'Public'

        # Special A
        elif self.octets[0] in classes['a']['special']:
            self.ip_class = 'A'
            self.designation = 'Special'

        # Private B
        elif self.octets[0] in classes['b']['private'][0] and (
                self.octets[1] in classes['b']['private'][1]):
            self.ip_class = 'B'
            self.designation = 'Private'

        # Public B
        elif self.octets[0] in classes['b']['public']:
            self.ip_class = 'B'
            self.designation = 'Public'

        # Private C
        elif self.octets[0] in classes['c']['private']:
            self.ip_class = 'C'
            self.designation = 'Private'

        # Public C
        elif self.octets[0] in classes['c']['public']:
            self.ip_class = 'C'
            self.designation = 'Public'

        # Class D
        elif self.octets[0] in classes['d']['private']:
            self.ip_class = 'D'
            self.designation = 'Private'

            # Class E
        elif self.octets[0] in classes['e']['private']:
            self.ip_class = 'E'
            self.designation = 'Private'




    def __str__(self):
        # return f"IP: {self.octets}, Subnet Mask: {self.mask}"
        return f"Output: Class: {self.ip_class}, Designation: {self.designation}"
