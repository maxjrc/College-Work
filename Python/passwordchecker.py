# password checker that tells you your level of password strength
import requests
import math

def enter_password():
    password = input("Enter your password: ")
    check_password(password)
    return password

def check_password(password):
    level = 0
    if len(password) > 8:
        level = level + 1
        if any(char.isdigit() for char in password):
            level = level + 1
            if any(not char.isalnum() for char in password):
                level = level + 1
                if any(char.isupper() for char in password):
                    level = level + 1
                    if any(char.islower() for char in password):
                        level = level + 1
                        print("Password strength is: ", level)
                    else:
                        reason = 'There are no lowercase letters!'
                        failed(reason)
                else:
                    reason = 'There are no upper case letters!'
                    failed(reason)
            else:
                reason = "There is no Special Charecters"
                failed(reason)
    else:
        reason = 'Password too short!'
        failed(reason)


def failed(reason):
    print("Password Check Failed. Reason: ", reason)
    ask = input("May I generate you a secure password? Y/N ")
    if(ask == "Y"):
        generate_password()
    if(ask == "N"):
        enter_password()
    
def generate_password():
    url = 'https://www.psswrd.net/api/v1/password/?length=17&lower=1&upper=0&int=1&special=0'
    sentrequest = requests.get(url)
    pass_json = sentrequest.json()
    newpassword = pass_json['password']
    print("Here is a new secure password: ", newpassword)


enter_password()