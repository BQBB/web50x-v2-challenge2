import re
from tabnanny import check
# the ip adress validator

ip_address = re.compile(r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\\    check = re.fullmatch(ip_address, user_input)
$''')

# check if the input is an ip adress
def ip_address_valid(check):    
    if check :
        return True
    return False
user_input = input("Enter an Ip address: ")
#print(mask_index)
if "\\" in user_input :
    mask_index = user_input.index('\\')
    check = re.fullmatch(ip_address, user_input)
else :
    check = re.fullmatch(ip_address, user_input)

first_group = int(user_input[:user_input.index(".")])
lst = [i for i, x in enumerate(user_input) if x == "."]
second_group = int(user_input[lst[0]+1:lst[1]])

# function that checks the Ip class
def check_class() :
    ip_class = ''
    if first_group < 128 :
        ip_class = 'A'
    elif first_group < 192 :
        ip_class = 'B'
    elif first_group < 224 :
        ip_class = 'C'
    elif first_group < 240 :
        ip_class = 'D'
    elif first_group < 239 :
        ip_class = 'E'
    return ip_class
the_class = check_class()
# function that checks the ip designation
def check_designation() :
    if the_class == "A" and first_group == 127 :
        return "Special Ip"
    if the_class == "A" and first_group == 10 :
        return "Private"
    elif the_class == "B" and first_group == 172 and second_group > 15 and second_group < 32 :
        return "Private"
    elif the_class == "C" and first_group == 192 and second_group == 168 :
        return "Private"
    elif the_class =="D" :
        return "Multicast"
    elif the_class == "E":
        return "Special"
    else:
        return "Public"

if ip_address_valid(check) :
    the_class = check_class()
    designation = check_designation()
    print(f"Class: {the_class}, Designation: {designation}")
else :
    print("You wrote a wrong Ip address or mask.")
