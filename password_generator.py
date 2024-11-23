import random
import string

def generate_password(length):
    if length <= 0:
        print("Invalid length.")
        return None

    password = ""
    options = [string.ascii_letters,string.digits,string.punctuation]

    while len(password) != length:
        j = random.randrange(0,3)
        char = options[j][random.randrange(0,len(options[j]))]
        password += char

    return password


print(generate_password(10))

