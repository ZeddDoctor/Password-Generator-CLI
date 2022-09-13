import random
import sys


def usr_inp():
    usr_inp_length = int(input("Decide length,minimum 5: \n\n"))
    print()
    usr_inp_choice = input("1.Alphabets,numbers and symbols\n2.Only numbers\n3.Alphabets and numbers\n0.Exit: \n\n")
    print()
    return usr_inp_length,usr_inp_choice

def convert(length,choice):
        length = int(length)
        choice = int(choice)

        return length,choice

def errors(length,choice):
        if length<5:
            sys.exit("Error: Length given is less than 5")

        if choice<0:
            sys.exit('Invalid choice')
        if choice>3:
            if choice!=8 or choice!=9:
                sys.exit('Invalid choice')


def gen_password(n,alpha_state,symbol_state):
    r_alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r_symbols = r'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    r_numbers = "0123456789"
    final_list=[]
    password=""
    c=0


    if alpha_state==False:#alpha_state is false only when all numbers option is selected
        password = r_numbers
        password = random.sample(password, len(password))
        return ("".join(password))

    if symbol_state==False and alpha_state==True:
        final_list = [r_alphabets,r_numbers]

    if symbol_state==True:#symbol state is true only when the all option is selected
        final_list = [r_alphabets, r_numbers, r_symbols]

    c = 0
    while c!=n+1:
        rand1 = random.randrange(0, len(final_list))#to choose randomly between the 3 or 2 choices in the list
        temp = final_list[rand1]
        rand2 = random.randrange(0, len(temp))#to choose a random character from the choice
        password += temp[rand2]
        c+=1
    return password

def main():
    try:
        length,choice = usr_inp()
        length,choice = convert(length, choice)
        errors(length, choice)
        
    except(TypeError,UnboundLocalError,ValueError):
        print("Invalid input")
        sys.exit()

    f=0
    while choice!=0:
        if choice ==1:
            print(gen_password(length, True, True))
            f=1

        if choice ==2:
                print(gen_password(length, False, False))
                f=1

        if choice ==3:
                print(gen_password(length, True, False))
                f=1

        if choice ==0:
            f=0
            print("Sayonara")
            system.exit()

        if f==1:
            choice_copy = choice
            choice = int(input("8.Generate again with same choices\n9.Generate with different choice\n0.Exit\n\n"))
        
        if choice ==8:
            choice = choice_copy

        if choice ==9:
            try:
                length,choice = usr_inp()
                length,choice = convert(length, choice)
                errors(length, choice)        
            except(TypeError,UnboundLocalError,ValueError):
                print("Invalid input")


    if choice==0:
        print("Sayonara")
            

main()