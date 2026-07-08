# Password Generator

## Description

A command line password generator that creates a random password based on the user's selected options. The user chooses the password length and whether to include uppercase letters, lowercase letters, special symbols, and numbers. The generated password is shuffled before being displayed.

## How to Run

```bash
python password_generator.py
```

## Sample Outputs

### Example 1: All Character Types

```text
Enter the length for the password: 12

Do you want the password to include uppercase letters?(y/n): y
Do you want the password to include lowercase letters?(y/n): y
Do you want the password to include special symbols?(y/n): y
Do you want the password to include numbers?(y/n): y

The generated password is 8@Pw2g!KqLm#
Thank you for using the service.
```

---

### Example 2: Uppercase and Numbers Only

```text
Enter the length for the password: 10

Do you want the password to include uppercase letters?(y/n): y
Do you want the password to include lowercase letters?(y/n): n
Do you want the password to include special symbols?(y/n): n
Do you want the password to include numbers?(y/n): y

The generated password is 4YB0T9P7QW
Thank you for using the service.
```

---

### Example 3: Lowercase Only

```text
Enter the length for the password: 8

Do you want the password to include uppercase letters?(y/n): n
Do you want the password to include lowercase letters?(y/n): y
Do you want the password to include special symbols?(y/n): n
Do you want the password to include numbers?(y/n): n

The generated password is qxmfjpta
Thank you for using the service.
```

---

### Example 4: Special Symbols and Numbers

```text
Enter the length for the password: 9

Do you want the password to include uppercase letters?(y/n): n
Do you want the password to include lowercase letters?(y/n): n
Do you want the password to include special symbols?(y/n): y
Do you want the password to include numbers?(y/n): y

The generated password is 7@1!58_#%
Thank you for using the service.
```

---

### Example 5: No Category Selected

```text
Enter the length for the password: 10

Do you want the password to include uppercase letters?(y/n): n
Do you want the password to include lowercase letters?(y/n): n
Do you want the password to include special symbols?(y/n): n
Do you want the password to include numbers?(y/n): n

Please choose atleast one from the given categories:

Do you want the password to include uppercase letters?(y/n): y
Do you want the password to include lowercase letters?(y/n): y
Do you want the password to include special symbols?(y/n): n
Do you want the password to include numbers?(y/n): y

The generated password is A7kR2mLpQ1
Thank you for using the service.
```

## Features

- User chooses password length.
- User can include uppercase letters.
- User can include lowercase letters.
- User can include special symbols.
- User can include numbers.
- Ensures at least one category is selected.
- Randomly shuffles the password before displaying it.
