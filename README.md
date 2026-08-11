# ATM Machine

A simple terminal-based ATM machine program that uses a PIN to authenticate the user and provides basic ATM operations through a menu.

## What it does

* Displays a welcome message
* Asks the user to enter a PIN before accessing the ATM
* Allows up to 3 incorrect PIN attempts before locking the account
* Grants access when the correct PIN is entered
* Displays a menu with different ATM options
* Validates the selected option and asks again if an invalid option is entered
* Allows the user to check their current balance
* Allows the user to withdraw money if sufficient balance is available
* Updates the balance after a successful withdrawal
* Lets the user exit the ATM program

### Current Options

| Option | Feature        |
| ------ | -------------- |
| 1      | Check Balance  |
| 2      | Withdraw Money |
| 3      | Exit           |
| 4      | Coming soon    |

## How to run it

```bash
python atm.py
```

Enter your PIN when prompted. You have 3 attempts to enter the correct PIN. After successful authentication, the ATM menu will be displayed.

Choose an option from the menu to check your balance, withdraw money, or exit the program.

## Current Status

The project is currently under development. PIN authentication, attempt limits, balance checking, money withdrawal, input validation, and the exit option have been implemented.

More features and ATM operations can be added as the project is developed further.

## What I learned building this

* Taking user input using `input()`
* Using `if` statements for PIN authentication and ATM operations
* Using `while` loops for PIN attempts and menu validation
* Limiting the number of incorrect PIN attempts
* Using `exit()` to stop the program when the account is locked
* Updating a variable after a successful money withdrawal
* Validating user input before processing an ATM option
* Structuring a program into different stages: authentication → menu → operations
