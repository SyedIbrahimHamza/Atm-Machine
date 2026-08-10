# ATM Machine

A simple terminal-based ATM machine program that uses a PIN to authenticate the user and provides a menu of ATM options.

## What it does

* Displays a welcome message
* Asks the user to enter a PIN
* Checks whether the entered PIN is correct
* Grants access when the correct PIN is entered
* Displays ATM options after successful login
* Validates the selected option and asks again if an invalid option is entered

### Current Options

| **Option** | **Feature**    |
| ---------- | -------------- |
| 1          | Check Balance  |
| 2          | Withdraw Money |
| 3          | Coming soon    |
| 4          | Coming soon    |

## How to run it

```bash
python atm.py
```

Enter your PIN when prompted. If the PIN is correct, the ATM menu will be displayed.

## Current Status

The project is currently under development. At this stage, PIN authentication and the basic ATM menu have been implemented.

More features such as checking balance, withdrawing money, and additional ATM operations will be added as the program is developed.

## What I learned building this

* Taking user input using `input()`
* Using `if` statements for PIN authentication
* Using `while` loops for input validation
* Displaying menu options in a terminal program
* Building an ATM program step by step
* Structuring a program into different stages: authentication → menu → operations
