correct_pin = "9876"
balance = 0
attempts = 3

print("Welcome to the ATM Machine!")
print("Please enter your PIN to continue:")

while attempts > 0:
    pin = input("Enter your PIN: ")
    
    if pin == correct_pin:
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("You have entered the wrong PIN 3 times. Your account is now locked.")
            exit()  # Program yahin band ho jayega
        else:
            print("Incorrect PIN. You have", attempts, "attempts left.")


print("Access granted!")


while True:
    print("\nPlease select an option:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    
    option = input("Enter your choice (1-4): ")
    
    
    while option not in ["1", "2", "3", "4"]:
        print("Invalid option. Please select a valid option:")
        option = input("Enter your choice (1-4): ")
    
    
    if option == "1":
        print("Your balance is:", balance)
    
    elif option == "2":
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print("Withdrawal successful! New balance:", balance)
    
    elif option == "3":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful! New balance:", balance)
    
    elif option == "4":
        print("Thank you for using our ATM. Goodbye!")
        break
