# Banking program
# Show Balance, Deposit, withdraw

program_name = "BANKING PROGRAM"
balance = 0
def show_balance():
    print(f"Balance: {balance}")

def deposit(money):
    global balance
    balance += money # if I assign to balance, python treats it as local variale

def withdraw(money):
    global balance
    balance -= money

def main():
    print("-" * 20)
    print(program_name)
    print("-" * 20)
    print()
    print("-" * 20)
    print("Rules:")
    print("-" * 20)
    print("Enter 0 to deposit:")
    print("Enter 1 to withdraw:")
    print("Enter 2 to show balance:")
    print("-" * 20)

    user_choice = input("Enter your choice: ")

    match user_choice:
        case "0":
            amount = int(input("Enter amount to deposit: "))
            deposit(amount)
            show_balance()
        case "1":
            amount = int(input("Enter amount to withdraw: "))
            withdraw(amount)
            show_balance()
        case "2":
            show_balance()
        case _:
            print("Invalid input")

if __name__ == '__main__':
    main()