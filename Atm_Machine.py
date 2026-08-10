print("Welcome to the ATM Machine!")
print ("Please enter your PIN to contnue:")
pin=input()
if pin=="8965":
    print("Access granted!")
    print("Please select an option:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    option=input()
    while option!=["1","2","3","4"]:
        print("Invalid option. Please select a valid option:")
        option=input()