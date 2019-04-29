import random
import string

def auto_url():
    char = string.ascii_letters+string.digits
    code = ''
    for i in range(6):
        code+=random.choice(char)
    return code
