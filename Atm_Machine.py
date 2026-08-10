print("Welcome to the ATM Machine!")
print ("Please enter your PIN to contnue:")
attempts=3

while attempts>0:
        pin=input()
        if pin=="9876":
            break
        else:
            attempts-=1
            if attempts==0:
                 print("You have entered the wrong PIN 3 times. Your account is now locked.")
            else:
                print("Incorrect PIN. You have", attempts, "attempts left.")


print("Access granted!")
print("Please select an option:")
print("1. Check Balance")
print("2. Withdraw Money")
option=input()
while option not in ["1","2","3","4"]:
    print("Invalid option. Please select a valid option:")
    option=input()
