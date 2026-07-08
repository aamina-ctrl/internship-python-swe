# Password Generator

## Description

A command line application that generates a secure random password based on user selected criteria.

The user can choose:
- Password length
- Include uppercase letters
- Include lowercase letters
- Include numbers
- Include special characters

The generated password always contains at least one character from every selected category.

---

## How to Run

```bash
python password_generator.py
```

---

## Sample Outputs

### Example 1

```
Enter password length: 12

Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y

Generated Password:
A#7kLm9!Px2Q
```

### Example 2

```
Enter password length: 16

Include uppercase letters? (y/n): n
Include lowercase letters? (y/n): y
Include numbers? (y/n): n
Include special characters? (y/n): y

Generated Password:
m@k!q#r%z&w*tp^
```

### Example 3

```
Enter password length: 10

Include uppercase letters? (y/n): n
Include lowercase letters? (y/n): n
Include numbers? (y/n): n
Include special characters? (y/n): n

Please select at least one character type.

```
---

## Notes

- Every generated password is random.
- The output will be different each time the program runs.
- The password includes at least one character from each selected category.
- Every generated password is random.
- The output will be different each time the program runs.
- The password includes at least one character from each selected category.
