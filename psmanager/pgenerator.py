import random

def generatePassword():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'
    symbols = '`~!@#$%^&*()_+=-{[]}\\|":;.,?/'

    all = lower + upper + numbers + symbols
    length = 16
    return ''.join(random.sample(all, length))

def savePassword(password):
    try:
        f = open("password.txt", "w")
        f.write(f"Generated Password: {password}")
        print("Successfully saved your password in password.txt!")
    except:
        raise Exception("Could not save your generated password.")
