
balance = 5000  
pin = 1234  
def check_balance():
    print(f"\nYour current balance is: ${balance:.2f}")
def deposit_money():
    global balance
    amount = float(input("\nEnter the amount to deposit: $"))
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} deposited successfully!")
        check_balance()
    else:
        print("Invalid deposit amount!")
def withdraw_money():
    global balance
    amount = float(input("\nEnter the amount to withdraw: $"))
    
    if amount > balance:
        print("Insufficient balance! Please enter a lower amount.")
    elif amount > 0:
        balance -= amount
        print(f"${amount:.2f} withdrawn successfully!")
        check_balance()
    else:
        print("Invalid withdrawal amount!")
def change_pin():
    global pin
    old_pin = int(input("\nEnter your current PIN: "))
    
    if old_pin == pin:
        new_pin = int(input("Enter your new PIN: "))
        confirm_pin = int(input("Confirm your new PIN: "))
        
        if new_pin == confirm_pin:
            pin = new_pin
            print("PIN changed successfully!")
        else:
            print("PINs do not match! Try again.")
    else:
        print("Incorrect PIN! Access denied.")

def atm_menu():
    """Displays the ATM menu and handles user actions."""
    global pin
    
    # PIN authentication
    entered_pin = int(input("Enter your ATM PIN: "))
    
    if entered_pin != pin:
        print("Incorrect PIN! Access denied.")
        return
    
    while True:
        print("\n===== ATM MACHINE =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("Thank you for using our ATM. Have a great day!")
            break
        else:
            print("Invalid option! Please select a valid choice.")

if __name__ == "__main__":
    atm_menu()