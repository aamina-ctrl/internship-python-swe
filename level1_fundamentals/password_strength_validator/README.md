# Password Strength Validator

## Description

A command line application that evaluates the strength of a password based on:

- Minimum length of 8 characters
- Uppercase letters
- Lowercase letters
- Numbers
- Special symbols

The program displays:
- Password strength score (out of 4)
- Missing character categories
- Final password strength rating

---

## How to Run

```bash
python password_strength_validator.py
```

---

## Sample Outputs

### Example 1: Password Too Short

```
Enter your password:
abc123

The password is too short. It must contain atleast 8 characters.
```

---

### Example 2: Weak Password

```
Enter your password:
abcdefgh

The Strength Score is 1 out of 4.

Missing uppercase.
Missing Special Symbols
Missing numbers.

Password Strength Validator: WEAK PASSWORD.
```

---

### Example 3: Moderate Password

```
Enter your password:
Password

The Strength Score is 2 out of 4.

Missing Special Symbols
Missing numbers.

Password Strength Validator: MODERATE PASSWORD.
```

---

### Example 4: Strong Password

```
Enter your password:
Password123

The Strength Score is 3 out of 4.

Missing Special Symbols

Password Strength Validator: STRONG PASSWORD.
```

---

### Example 5: Very Strong Password

```
Enter your password:
Password123!

The Strength Score is 4 out of 4.

Password Strength Validator: VERY STRONG PASSWORD.
```

---

### Example 6: Missing Lowercase

```
Enter your password:
PASSWORD123!

The Strength Score is 3 out of 4.

Missing lowercase.

Password Strength Validator: STRONG PASSWORD.
```

---

### Example 7: Missing Uppercase

```
Enter your password:
password123!

The Strength Score is 3 out of 4.

Missing uppercase.

Password Strength Validator: STRONG PASSWORD.
```

---

## Notes

- Passwords must contain at least 8 characters.
- The maximum strength score is 4.
- One point is awarded for each of the following:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special symbols
- The program reports any missing character categories before displaying the final password strength.
