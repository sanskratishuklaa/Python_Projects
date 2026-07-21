import random
import string

passwords={}

#load exiting passwords
try:
    with open("password.txt", "r") as file:
        for line in file:
            website,pwd=line.strip().split(":")
            passwords[website]=pwd
except:
    pass

def generate_password():
    chars=string.ascii_letters+string.digits+"!@#$%&"