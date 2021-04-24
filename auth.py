from random import randrange
from datetime import datetime

database = {6118915185: ['Omoluabi', 'Alakowe', 'alakowe@gmail.com', 'pass', 10000]}

def init():
    print(f"{'*' * 25}\n   Welcome to bank PHP\n{'*' * 25}")

    option_selected = int(input("\nDo you have an account with us? (1) Yes (2) No (3) End \n"))
    if option_selected == 1:
        login()
        
    elif option_selected == 2:
        register()
        
    elif option_selected == 3:
        end_program()
        
    else:
        print("\nInvalid option selected, try again!")
        init()


def login():
    option_selected = int(input("\nSelect an option: (1) Login (2) Homepage (3) End \n"))

    if option_selected == 1:
        print("\n********* Login *********")

        user_account_number = int(input("Enter your account number: \n"))

        for account_number, user_details in database.items():
            if user_account_number == account_number:
                password = input("Enter your password: \n")

                if password == user_details[3]:
                    bank_operations(user_details)
                
        else:
            print("Incorrect account number or password.")
            login()

    elif option_selected == 2:
        homepage()
        
    elif option_selected == 3:
        end_program()
        
    else:
        print("Invalid option selected, try again!")
        login()


def register():
    option_selected = int(input("Select an option: (1) Register (2) End \n"))

    if option_selected == 1:
        print("\n********* Register *********")

        email = input("Please enter your email address: \n")
        first_name = input("Please enter your first name: \n")
        last_name = input("Please enter your last name: \n")
        user_password = password()
        account_balance = 0     # Initializing user account balance to zero

        # Taking care of the chance the user leaves any of the input fields empty
        if email == '' or first_name == '' or last_name == '' or user_password == '' or user_password == '':
            print("\nUnfilled detail(s) detected! Please ensure no input field is left empty.")
            register()
            
        else:
            account_number = account_number_generation()
            database[account_number] = [first_name, last_name, email, user_password, account_balance]

            print(f"\nAccount creation successful!\n{'=' * 35}\n Your account number is {account_number}\n{'=' * 35}")
            print("Please keep your details safe.")
            login()
        
    elif option_selected == 2:
        end_program()

    else:
        print("Invalid option selected, try again!")
        register()


def bank_operations(user):    
    print(f"\n********* Welcome {user[0]} {user[1]} ********* ")
    print(datetime.now().strftime("%d-%B-%Y   %I:%M:%S %p"))

    option_selected = int(input("\nSelect an option: (1) Withdrawal (2) Cash Deposit (3) Transfer (4) Check Balance (5) Complaint (6) Logout (7) End \n"))
    if option_selected == 1:
        withdrawal_operation(user)
        login()
        
    elif option_selected == 2:
        cash_deposit_operation(user)
        login()
        
    elif option_selected == 3:
        transfer_operation(user)
        login()

    elif option_selected == 4:
        balance_operation(user)
        login()
        
    elif option_selected == 5:
        complaint_operation()
        login()
        
    elif option_selected == 6:
        logout()
        
    elif option_selected == 7:
        end_program()
        
    else:
        print("Invalid option selected, please try again")
    

def withdrawal_operation(user):
    amount_to_withdraw = int(input("How much would you like to withdraw? \n"))

    if amount_to_withdraw <= user[4]:
        user[4] -= amount_to_withdraw  # updating the user's account balance.
        print(f"Take your cash (₦{amount_to_withdraw})! Your account balance is now ₦{user[4]}.")
        print("\nDo you want to perform another action?")

    else:
        print("Insufficient funds")


def cash_deposit_operation(user):
    amount_deposited = int(input("How much would you like to deposit? \n"))
    user[4] += amount_deposited
    print(f"Your current balance is now ₦{user[4]}")
    print("\nDo you want to perform another action?")


def transfer_operation(user):
    amount_to_transfer = int(input("How much would you like to transfer? \n"))
    recipient_account = int(input("Enter account number: \n"))
    recipient_bank = input("Enter recipient bank: \n")
    user_password = input("Enter your password: \n")

    if user_password == user[3]:
        if amount_to_transfer <= user[4]:
            user[4] -= amount_to_transfer
            print(f"Transfer successful! Your account balance is now ₦{user[4]}")
            print("\nDo you want to perform another action?")

        else:
            print("Insufficient funds")

    else:
        print("Incorrect password.")


def balance_operation(user):
    print(f"Your balance is ₦{user[4]}.")
    print("\nDo you want to perform another action?")

    
def complaint_operation():
    complaint = input("What issue will you like to report? \n")
    print("Thank you for contacting us, your issue will be resolved.")
    print("\nDo you want to perform another action?")


def password():
    new_password = input("Please enter your new password: \n")
    confirm_password = input("Please confirm password: \n")

    if new_password == confirm_password:
        return new_password
    
    else:
        print("\nPassword does not match. Please try again.")
        password()


def account_number_generation():
    account_number = randrange(1111111111, 9999999999)
    if account_number in database.keys():
        account_number_generation()
    else:
        return account_number


def logout():
    login()


def homepage():
    init()

    
def end_program():
    print("\nThank you for banking with us!")
    exit()


init()
