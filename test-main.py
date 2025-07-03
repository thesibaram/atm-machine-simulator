from tests.test_account import Account
from tests.test_atm_machine import AtmMachine
from tests.test_transaction import Transaction

is_on = True

def main():
    global is_on
    a = Account("Clara", 990077554422, 1437, 7850)
    b = AtmMachine()
    c = Transaction(a)

    while is_on:
        b.menu()
        try:
            option = int(input("Enter the option you want: "))
            if option == 1:
                while True:
                    try:
                        amount = int(input("How much money do you want to deposit: "))
                        if amount >= 0:
                            c.deposit(amount)
                            break
                        else:
                            print("Transaction failed: The deposit amount must be at least 1.")
                    except ValueError:
                        print("Kindly enter a valid amount.")
            elif option == 2:
                while True:
                    try:
                        amount = int(input("How much money do you want to withdraw: "))
                        c.withdraw(amount)
                        break
                    except ValueError:
                        print("Kindly enter a valid amount.")
            elif option == 3:
                while True:
                    try:
                        amount = int(input("How much money do you want to transfer: "))
                        acc_no = int(input("Enter the account number you want to transfer to: "))
                        c.transfer(amount, acc_no)
                        break
                    except ValueError:
                        print("Kindly enter a valid input.")
            elif option == 4:
                c.check_balance()
            elif option == 5:
                c.get_transaction_history()
            elif option == 6:
                a.change_pin()
            elif option == 7:
                print("Exiting...")
                is_on = False
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError:
            print("Kindly enter a valid option.")
            continue

if __name__ == "__main__":
    main()
