
#to seperate user data into parts
def seperate_parts(name):
    parts=set()
    for start in range(len(name)):
            for end in range(len(name),start+2,-1):
                part=name[start:end]
                parts.add(part)
    return parts


def contains_user_data(password,user_data):
    issues=set()
    for name in user_data:
        name=name.lower()
        parts=seperate_parts(name)
        for part in parts:
            if part in password:
                issues.add(part)
    if issues:            
        return f"Password contains [ {max(issues , key=len)} ] part of user data"


def is_common_password(password,common_passwords):
    pwd = password.lower()
    for word in common_passwords:
        if word in pwd:
            return f"Password contains commonly used word [ {word} ]"

def check_length(password):
    length = len(password)
    if length < 8:
        return 0,"Password must be atleast 8 characters "
    elif length < 12:
        return 10,"Password length is acceptable but not strong (length less than 12)."
    elif length < 16:
        return 25,"Use atleast 16 characters for maximum protection."
    else:
        return 40,"Password has maximum protection (length > 16)."

def check_charset(password):
    score = 0
    issue=[]
    if any(c.islower() for c in password):
        score += 15
    else:    
        issue.append("Atleast one lowercase letter is required. ")
    if any(c.isupper() for c in password):
        score += 15
    else:    
        issue.append("Atleast one uppercase letter is required. ")
    if any(c.isdigit() for c in password):
        score += 15
    else:    
        issue.append("Atleast one digit is required. ")
    if any(not c.isalnum() for c in password):
        score += 15
    else:    
        issue.append("Atleast one special character is required. ")
    return score,issue


def has_repetition(password):
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return f"Password has repeated characters [ {password[i]} (-20)."
    return False


def has_sequence(password):
    sequences = "abcdefghijklmnopqrstuvwxyz0123456789asdfghkl;qwertyuiop[]zxcvbnm,."
    pwd = password.lower()

    for i in range(len(sequences) - 3):
        if sequences[i:i+4] in pwd:
            return f"Password has sequence [ {sequences[i:i+4]} ] (-20)."
    return False
    
