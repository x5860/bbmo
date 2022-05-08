import random
def password_generator():
    pas = ''
    symbols = list('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ!#$%&()*+,-./:;<=>?@[\]^_`{|}~')
    for x in range(random.randrange(8, 32, 1)):
        pas = pas + random.choice(symbols)
    return (f'Your password is: {pas}. Password length: {len(pas)} symbols')
print(password_generator())
