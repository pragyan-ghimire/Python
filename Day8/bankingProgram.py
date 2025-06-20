# Banking program
# Show Balance, Deposit, withdraw
import sys

program_name = "BANKING PROGRAM"
balance = {}
authentication = {}
logged_in = False
logged_in_user = ""

def show_balance(user):
    return balance.get(user)

def deposit(user, amount):
    amount = amount + balance.get(user)
    balance.update({user: amount})

def withdraw(user, amount):
    if(balance.get(user) > amount):
        balance.update({user: balance.get(user)-amount})
    else:
        print("Cannot withdraw. Insufficient balance")

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

def login():
    global logged_in
    global logged_in_user

    print("--------------Log IN--------------")
    user_name = input("Enter your username: ")
    if user_name in authentication.keys():
        password = input("Enter your password: ")
        if password == authentication.get(user_name):
            logged_in = True
            logged_in_user = user_name
            print("Access Granted.")
            print(f"{logged_in_user} is logged in.")
            print() 
        else:
            print("Access Denied.")
            print()
            exit_program()
    else:
        print("User not available.")
        exit_program()
    
def home():
    print("----------------------------------")
    print("Login (Enter L): ")
    print("Create account (Enter A): ")
    print("Enter any key to exit: ")
    print("----------------------------------")
    print()
    entry_choice = input("Enter your choice: ").upper()

    if entry_choice == "L":
        login()
    elif entry_choice == "A":
        print("--------------Create Account--------------")
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")
        print()
        authentication.update({user_name: password})
        balance.update({user_name: 0})
        login()
    else:
        exit_program()

def main():
    global logged_in
    global logged_in_user

    print("-" * 20)
    print(program_name)
    print("-" * 20)
    print()
    print("-" * 20)
    print("Some Guidline to Follow After Logging IN:")
    print("-" * 20)
    print("Enter 0 to deposit:")
    print("Enter 1 to withdraw:")
    print("Enter 2 to show balance:")
    print("Enter Q to exit: ")
    print("-" * 20)
    print()
    print()

    home()

    while logged_in:
        user_choice = input("Enter your choice: ").upper()

        match user_choice:
            case "0":
                amount = int(input("Enter amount to deposit: "))
                deposit(logged_in_user, amount)
                print(f"Your current balance is {show_balance(logged_in_user)}")
                print()

            case "1":
                amount = int(input("Enter amount to withdraw: "))
                withdraw(logged_in_user, amount)
                print(f"Your current balance is {show_balance(logged_in_user)}")
                print()

            case "2":
                print(f"Your current balance is {show_balance(logged_in_user)}")
                print()

            case "Q":
                logged_in = False
                home()

            case _:
                print("Invalid input")

if __name__ == '__main__':
    main()