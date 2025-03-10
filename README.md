# PSmanager Release 0.0.1
This is a python package which helps managing passwords.

## Features
* It can create random passwords using - **createPassword()**
* It can do checks for the password's strength using - **checkPasswordStrength()**
* It can save passwords securely using - **savePassword()**
* More features will be added in future

# Installation
Do ```pip install psmanager``` in your terminal to install the latest version of __**psmanager**__.

# How to use it?
To use this package, create a ```.py``` file and type ```import psmanager``` or ```from psmanager import <function name>```.

### generatePassword()
Generates a 14 characters long random but very strong and hard to guess password for your systems and accounts. 

for example :-
### Code
```
import psmanager
password = psmanager.generatePassword()  # This returns a string

print("Random Generated Password: ", password)
```
### Output
```
Random Generated Password: xqzlvu03519*bq
```    

### savePassword()
Saves your randomly generated password in `password.txt`.  

for example :- 
### Code
```
import psmanager
password = psmanager.generatePassword()
psmanager.savePassword(password)
```
### Output
`On Console`
```
Successfully saved your password in password.txt!
```
`In password.txt`
```
Generated Password: ryixtp44997@nv
```

### checkPasswordStrength()
Runs a check for password's strength. This returns a tuple (bool, string - "Strong", "Moderate" or "Weak")  

for example :-
#### 1)
### Code
```
import psmanager
randomPassword = psmanager.generatePassword()
passwordStrength = psmanager.checkPasswordStrength(randomPassword)  # This returns a tuple (bool, string)

print(passwordStrength[1])  # We only need the string, so using index 1
```
### Output
Lets assume that random password generated is `password@1xyz`
```
Strong
```
Lets assume that random password generated is `passwd@1xyz`
```
Moderate
```
Lets assume that random password generated is `password@1`
```
Weak
```

#### 2) 
### Code
```
import psmanager

passwordStrength = psmanager.checkPasswordStrength("password here")  # This returns a tuple (bool, string)

if passwordStrength[0]:  # To get the bool -> True or False
    print("pass")
else:
    print("fail")
```
### Output
Lets assume that the password is `passwd@1xyz` __a moderate password__
```
pass
```
Lets assume that the password is `passwd@yxz` __Not a good password__
```
fail
```

# License
> Copyright(c) 2022 Saaem Faridi  

`This repository is licensed under the MIT license. See LICENSE for details`.