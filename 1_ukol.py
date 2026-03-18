from itertools import count


def analyze_password(password="str", min_length=8, require_digit=True,
                     require_upper=True, require_symbol=False, banned_words=None):
    if len(password)>=min_length:

    # aspoň 1 číslo
    for i in password:
        counter = 0
        if i.isdigit():
            counter += 1
    if counter >= 1:
        return True

    #aspoň 1 velké písmeno
    for i in password:
        counter = 0
        if i.isupper():
            counter += 1
    if counter >= 1:
        return True

    # aspoň 1 symbol
    for i in password:
        smboly = "!@#$%^&*()-_=+[]{};:,.?"
        counter = 0
        if i in smboly:
            counter += 1
    if counter>=1
        return True

    if password in banned_words:
        return
