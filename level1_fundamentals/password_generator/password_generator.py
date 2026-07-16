import random

uppercase="ABCDEFGHIKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
special_symbols="!@#$%^&*()_"
numbers="0123456789"

length=int(input("Enter the length for the password: "))
while length < 4:
    print("Please enter a length greater than or equal to 4.")
    length=int(input("Enter the length for the password: "))

def user_choices():

    allowed_characters=""

    in_u=input("Do you want the password to include uppercase letters?(y/n): ")
    if in_u.lower()=="y":
        allowed_characters+=uppercase

    in_l=input("Do you want the password to include lowercase letters?(y/n): ")
    if in_l.lower()=="y":
        allowed_characters+=lowercase

    in_ss=input("Do you want the password to include special symbols?(y/n): ")
    if in_ss.lower()=="y":
        allowed_characters+=special_symbols

    in_num=input("Do you want the password to include numbers?(y/n): ")
    if in_num.lower()=="y":
        allowed_characters+=numbers

    password=""
    if (in_u.lower()=="y"):
        password+=random.choice(uppercase)
    if (in_l.lower()=="y"):
        password+=random.choice(lowercase)
    if (in_ss.lower()=="y"):
        password+=random.choice(special_symbols)
    if (in_num.lower()=="y"):
        password+=random.choice(numbers)
    return allowed_characters, password

allowed_characters,password=user_choices()
while allowed_characters=="":
    print("Please choose atleast one from the given categories:")
    allowed_characters,password=user_choices()

current_length= len(password)
length-=current_length

for i in range(length):
    password+=random.choice(allowed_characters)

password_list= list(password)
random.shuffle(password_list)
password="".join(password_list)

print(f"The generated password is {password} ")
print("Thank you for using the service.")
