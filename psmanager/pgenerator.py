import random

def generatePassword():
    alphabets = ["a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    specialCharacter = ["~","`","!","@","#","$","%","^","&","*","_"]

    return f"{random.choice(alphabets)}{random.choice(alphabets)}{random.choice(alphabets)}{random.choice(alphabets)}{random.choice(alphabets)}{random.choice(alphabets)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.choice(specialCharacter)}{random.choice(alphabets)}{random.choice(alphabets)}"

def savePassword(password):
    try:
        f = open("password.txt", "w")
        f.write(f"Generated Password: {password}")
        print("Successfully saved your password in password.txt!")
    except:
        raise Exception("Could not save your generated password.")