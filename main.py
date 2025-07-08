import os
import time
from prettytable import PrettyTable
from atm.account import Account
from atm.atm_machine import AtmMachine
from atm.transaction import Transaction
from atm.ascii_title import ascii_logo

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_and_header():
    """
    Clears the screen and redraws the ASCII logo.
    Keeps the logo persistent across all screens.
    """
    clear_screen()
    ascii_logo()
    print(color_text("-" * 60, "96"))

def welcome_message():
    clear_and_header()
    print(color_text("{:^60}".format("Welcome to the ATM System!"), "92"))
    print(color_text("-" * 60, "96"))
    time.sleep(1.5)

def main():
    is_on = True
    welcome_message()


    while True:
        name = input(color_text("Enter your name: ", "94")).strip()
        if not name:
            print(color_text("[!] Name cannot be empty.", "91"))
            continue
        break

    while True:
        try:
            acc_no = int(input(color_text("Enter your 12-digit account number: ", "94")))
            if len(str(acc_no)) != 12:
                raise ValueError
            break
        except ValueError:
            print(color_text("[!] Please enter a valid 12-digit account number.", "91"))

    while True:
        try:
            pin = int(input(color_text("Enter your 4-digit PIN: ", "94")))
            if len(str(pin)) != 4:
                raise ValueError
            break
        except ValueError:
            print(color_text("[!] Please enter a valid 4-digit PIN.", "91"))

    while True:
        try:
            bal = int(input(color_text("Enter the amount you wish to deposit: ", "94")))
            if bal < 0:
                raise ValueError
            break
        except ValueError:
            print(color_text("[!] Please enter a positive number.", "91"))

    print(color_text("[✓] Account created successfully!", "92"))
    time.sleep(1.2)

    a = Account(name, acc_no, pin, bal)
    print(color_text("Please set up your security question for account recovery.\n", "93"))
    a.security_question()
    b = AtmMachine()
    c = Transaction(a)

    while is_on:
        clear_and_header()

        table = PrettyTable()
        table.field_names = [color_text("Option", "95"), color_text("Action", "95")]
        table.add_rows([
            [1, "Deposit"],
            [2, "Withdraw"],
            [3, "Transfer"],
            [4, "Check Balance"],
            [5, "Transaction History"],
            [6, "Change PIN"],
            [7, "Forgot PIN"],
            [8, "Exit"]
        ])
        print(table)

        try:
            option = int(input(color_text("Select an option (1-8): ", "93")))
            if option < 1 or option > 8:
                raise ValueError

            if option == 1:
                clear_and_header()
                c.deposit()

            elif option == 2:
                clear_and_header()
                c.withdraw()

            elif option == 3:
                clear_and_header()
                c.transfer()

            elif option == 4:
                clear_and_header()
                c.check_balance()

            elif option == 5:
                clear_and_header()
                c.get_transaction_history()

            elif option == 6:
                clear_and_header()
                a.change_pin()

            elif option == 7:
                clear_and_header()
                a.forget_pin()

            elif option == 8:
                print(color_text("[✓] Thank you for using our ATM service. Goodbye!", "96"))
                time.sleep(1.5)
                is_on = False

        except ValueError:
            print(color_text("[!] Invalid input. Please enter a number between 1 and 8.", "91"))
            time.sleep(2)

if __name__ == "__main__":
    main()
