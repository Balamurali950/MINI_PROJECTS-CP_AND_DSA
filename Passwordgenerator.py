import random
import string
print("Welcome to Password generator")
n_letter=int(input("How many letters do you want in password:"))
n_num =int(input("How many numbers do you want in password:"))
n_symbol =int(input("How many symbols do you want in password:"))
password_list = []
for i in range(n_letter):
    password_list += random.choice(string.ascii_letters)
for i in range(n_num):
    password_list += random.choice(string.digits)
for i in range(n_symbol):
    password_list += random.choice(string.punctuation)
random.shuffle(password_list)
password=""
for i in password_list:
    password += i
print("This is your password as per your requirements:\n",password)