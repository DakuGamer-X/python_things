import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    chars = letters + digits + symbols
    password = ''.join(random.choice(chars) for i in range(length))
    return password

print(generate_password(16))
