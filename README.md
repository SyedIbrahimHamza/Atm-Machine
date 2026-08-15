# ATM Machine

A simple terminal-based ATM machine program written in Python that uses PIN authentication and provides basic banking operations through a menu.

## What it does

* Displays a welcome message
* Asks the user to enter a PIN before accessing the ATM
* Allows up to 3 incorrect PIN attempts before locking the account
* Grants access when the correct PIN is entered
* Displays an ATM menu with different options
* Validates the selected option and asks again if an invalid option is entered
* Allows the user to check their current balance
* Allows the user to withdraw money if sufficient balance is available
* Validates withdrawal amounts before processing
* Prevents withdrawals when the balance is insufficient
* Allows the user to deposit money into their account
* Validates deposit amounts before processing
* Updates the balance after successful withdrawals and deposits
* Lets the user exit the ATM program

## Current Options

| Option | Feature        |
| ------ | -------------- |
| 1      | Check Balance  |
| 2      | Withdraw Money |
| 3      | Deposit Money  |
| 4      | Exit           |

## Input Validation

The program includes validation for different types of user input:

* Checks whether the entered PIN is correct
* Limits the user to 3 incorrect PIN attempts
* Validates that the selected ATM option is between 1 and 4
* Allows only numeric values for withdrawals and deposits
* Prevents users from entering zero or negative amounts
* Prevents withdrawals when the requested amount is greater than the available balance
* Continues asking for valid input when an invalid amount is entered

## How to run it

```bash
python Atm_Machine.py
```

Enter your PIN when prompted. You have 3 attempts to enter the correct PIN. After successful authentication, the ATM menu will be displayed.

Choose an option from the menu to check your balance, withdraw money, deposit money, or exit the program.

The account starts with a balance of `0`.

## Current Status

The project is currently under development. PIN authentication, attempt limits, balance checking, money withdrawal, money deposits, input validation, insufficient-funds checking, and the exit option have been implemented.

More features and ATM operations can be added as the project is developed further.

## What I learned building this

* Taking user input using `input()`
* Using `if` and `elif` statements for PIN authentication and ATM operations
* Using `while` loops for repeated input and validation
* Validating user input before processing an option
* Using `.isdigit()` to validate numeric input
* Using a variable to store and update the account balance
* Using `break` to exit loops after valid input
* Using `continue` to repeat the input process when invalid data is entered
* Using `exit()` to stop the program when the account is locked
* Using a counter to limit the number of PIN attempts
* Performing basic arithmetic operations for withdrawals and deposits
* Checking available balance before allowing a withdrawal
* Structuring a program into different stages: authentication → menu → operations → exit
