import string
import random

characters=list(string.ascii_letters+string.digits+string.punctuation)

def generatepass():
    passwordlength=int(input("how long you want to be your password\n"))

    random.shuffle(characters)
    password=[]
    for i in range(passwordlength):
        password.append(random.choice(characters))

    random.shuffle(password) 
    
    password="".join(password)
    print(password)

option=input("do you want to generate a password (Yes/No)")

if option=="Yes":
    generatepass()
elif option=="No":
    print("program ended")
    quit()
else:
    print("Invalid input")
    quit()
