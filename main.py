from checker import evaluate_password
from validators import (
    is_valid_name,
    is_valid_email,
    is_valid_DOB,
    is_valid_phone
    )

def load_common_passwords():
    with open('common_passwords.txt','r') as f:
        passwords = []
        for line in f:
            passwords.append(line.strip().lower())
        return set(passwords)    

def main():
    print("=== Password Strength Checker (CLI) ===")
    user_data=[]
    Password = input("Enter your password : ")
    while True:
        name = input("Enter your name : ")
        if is_valid_name(name):
            break
        print("Invalid name try again. ")
    while True:    
        DOB = input("Enter your DOB (YYYYMMDD) : ")
        if is_valid_DOB(DOB):
            break
        print("Invalid DOB try again. ")
    while True:   
        email = input("Enter your email id : ")
        if is_valid_email(email):
            break
        print("Invalid email address try again. ")
    while True:   
        phone_no = input("Enter your phone no : ")
        if is_valid_phone(phone_no):
            break
        print("Invalid phone no try again. ")

    user_data=[name,DOB,email,phone_no]
    common_passwords = load_common_passwords()

    result = evaluate_password(Password,user_data,common_passwords)

    print("\nResult:")
    print("Status:", result["status"])

    if result["status"] == "UNSAFE":
        print("Reasons:")
        for r in result["reasons"]:
            print("-> ", r)
    else:
        print(f"Strength: {result['strength']} ({result['score']}/100)")
        if result["notes"]:
            print("Notes:")
            for n in result["notes"]:
                print("-> ", n)

if __name__=="__main__":
    main()                