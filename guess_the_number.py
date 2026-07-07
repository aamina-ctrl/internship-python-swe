import random

secret_number=random.randint(0,9)

for attempts in range (0,3):
    user_guessed=int(input(f"ATTEMPT {attempts+1}: Guess the number!: "))
    if user_guessed>secret_number:
        print("Too high!")
    elif user_guessed<secret_number:
        print("Too low!")
    else:
        print("Correct! You Won!")
        break
if user_guessed==secret_number:
    pass
    exit()
if user_guessed!=secret_number:
    print("Sorry. You lost.")
    print(f"All attempts have been used. The number was {secret_number}")


