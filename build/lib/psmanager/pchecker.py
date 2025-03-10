def checkSpecialCharacters(password: str):
    specialCharacter = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','"','\'','<',',','>','.','?','/']
    for char in specialCharacter:
        if char in password:
            return True
    return False

def checkPasswordLength(password: str):
    length = len(password)
    if 8 <= length <= 10:
        return 1
    elif 11 <= length <= 12:
        return 2
    elif 13 <= length <= 16:
        return 3
    else:
        return 0
'''
0 -> Invalid Password
1 -> Weak Password
2 -> Moderate Password
3 -> Strong Password
'''

def checkNums(password: str):
    for char in password:
        if char.isdigit():
            return True
    return False
        

def checkPasswordStrength(password: str):
    length_check = checkPasswordLength(password)
    special_char = checkSpecialCharacters(password)
    nums = checkNums(password)

    if length_check != 0:
        if length_check == 1:
            if special_char and nums:
                return "Weak Password"
            else:
                return "Very Weak Password"
        elif length_check == 2:
            if special_char and nums:
                return "Moderate Password"
            else:
                return "Weak Password"
        elif length_check == 3:
            if special_char and nums:
                return "Strong Password"
            else:
                return "Moderate Password"
    else:
        return "Invalid Password"
