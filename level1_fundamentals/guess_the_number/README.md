# Guess the Number

## Description
A command line number guessing game where the computer randomly selects a number between 0 and 9. The user has 3 attempts to guess the correct number. After each incorrect guess, the program tells the user whether the guess was too high or too low. If all attempts are used without guessing correctly, the correct number is displayed.

## How to Run

```bash
python guess_the_number.py
```

## Sample Outputs

### Correct on First Attempt

```
ATTEMPT 1: Guess the number!: 6
Correct! You Won!
```

### Correct on Second Attempt

```
ATTEMPT 1: Guess the number!: 8
Too high!

ATTEMPT 2: Guess the number!: 5
Correct! You Won!
```

### Correct on Third Attempt

```
ATTEMPT 1: Guess the number!: 2
Too low!

ATTEMPT 2: Guess the number!: 8
Too high!

ATTEMPT 3: Guess the number!: 5
Correct! You Won!
```

### User Loses

```
ATTEMPT 1: Guess the number!: 2
Too low!

ATTEMPT 2: Guess the number!: 7
Too high!

ATTEMPT 3: Guess the number!: 1
Too low!

Sorry. You lost.
All attempts have been used. The number was 5
```

## Features

- Random number generated between 0 and 9
- Three guessing attempts
- Indicates whether each guess is too high or too low
- Stops immediately when the correct number is guessed
- Displays the correct number if the user loses
