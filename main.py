from ip_address import IpAddress
def solution():
    print('Please enter an ip in this format x.x.x.x/x: ')
    user_input = input()

    ip = IpAddress.from_string(user_input)

    print(ip)


if __name__ == '__main__':
    solution()