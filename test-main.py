from tests.test_account import Account
from tests.test_atm_machine import AtmMachine
from tests.test_transaction import Transaction


is_on = True

def main():

    a = Account("Clara", 990077554422, 1437, 7850, )
    b = AtmMachine()
    c = Transaction()

    while is_on:
        b.menu()
        try:
            option = int(input("Enter the option you want: "))
            if option == 1:
                amount = int(input("How much money do you want to deposit: "))
                c.deposit(amount)
            else:
                print("Invalid Input")
        except:
            pass

if __name__ == "__main__":
    main()


