import random
def gen_name():
    abc = 'abcdefghijklmnopqrstuvwxyz'
    name = ''
    for i in abc:
        if len(name)<5:
            x = abc[random.randint(0, len(abc)-1)]
            name+=x
    return name.capitalize()

def gen_login():
    simb = 'abcdefghijklmnopqrstuvwxyz1234567890'
    first = ''
    second = ['ya.ru', 'gmail.com', 'mail.ru']
    login = ''
    for i in simb:
        if len(first)<5:
            x = simb[random.randint(0, len(simb)-1)]
            first+=x
    login = f'{first.capitalize()}@{second[random.randint(0, len(second)-1)]}'
    return login

def gen_password():
    simb = 'abcdefghijklmnopqrstuvwxyz!#$%^&*1234567890'
    password = ''
    for i in simb:
        if len(password)<6:
            x = simb[random.randint(0, len(simb)-1)]
            password+=x
    return password