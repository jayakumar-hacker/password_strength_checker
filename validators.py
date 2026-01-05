
def is_valid_name(name):
    name = name.strip()
    if len(name) < 3:
        return False
    if not name.isalpha():
        return False
    return True


def is_valid_email(email):
    email = email.strip()
    if " " in email:
        return False
    if email.count("@") != 1:
        return False

    user, domain = email.split("@")
    if not user or "." not in domain:
        return False

    return True


def is_valid_phone(phone):
    phone = phone.strip()
    if not phone.isdigit():
        return False
    if len(phone) != 10:
        return False
    if phone[0] not in "6789":
        return False
    return True

def is_valid_DOB(DOB):
    DOB = DOB.strip()
    if not DOB.isdigit():
        return False
    if len(DOB) != 8:
        return False
    return True