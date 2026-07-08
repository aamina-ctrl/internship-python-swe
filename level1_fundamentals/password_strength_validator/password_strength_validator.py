password=input("Enter your password:")

length=len(password)
if length<8:
    print("The password is too short. It must contain atleast 8 characters.")
    exit()

uppercase="ABCDEFGHIKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
special_symbols="!@#$%^&*()_"
numbers="0123456789"

has_uppercase=False
has_lowercase=False
has_ss=False
has_numbers=False

for char in password:
    if char in uppercase:
        has_uppercase=True
    if char in lowercase:
        has_lowercase=True
    if char in special_symbols:
        has_ss=True
    if char in numbers:
        has_numbers=True

strength=0

if has_uppercase:
    strength+=1
if has_lowercase:
    strength+=1
if has_ss:
    strength+=1
if has_numbers:
    strength+=1

print(f"The Strength Score is {strength} out of 4.")

if has_uppercase==False:
    print("Missing uppercase.")
if has_lowercase==False:
    print("Missing lowercase.")
if has_ss==False:
    print("Missing Special Symbols")
if has_numbers==False:
    print("Missing numbers.")

if strength==1:
    print("Password Strength Validator: WEAK PASSWORD.")
elif strength==2:
    print("Password Strength Validator: MODERATE PASSWORD.")
elif strength==3:
    print("Password Strength Validator: STRONG PASSWORD.")
else:
    print("Password Strength Validator: VERY STRONG PASSWORD.")


