import string
import random

lc=list(string.ascii_lowercase)
uc=list(string.ascii_uppercase)
dg=list(string.digits)
sp=list("!@#$%^&*+-")

def generate_random_password():
    pwd=[]
    length=int(input("Enter password length (8 or greater):"))
    random.shuffle(lc)
    random.shuffle(uc)
    random.shuffle(dg)
    random.shuffle(sp)
    
    if length>=8:
        for x in range(round(length*0.2)):
            pwd.append(random.choice(sp))
        for x in range(round(length*0.2)):
            pwd.append(random.choice(dg))
        for x in range((length-(round(length*0.2)*2))//2):
            pwd.append(random.choice(uc))
        for x in range(length-((round(length*0.2)*2)+(round(length*0.2)*2)//2)):
            pwd.append(random.choice(lc))
        random.shuffle(pwd)
        print("".join(pwd))

    else:
        print("\nKindly enter a value greater than 8")

generate_random_password()


