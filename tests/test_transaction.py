from tests.test_account import Account

class Transaction:
    def __init__(self, account: Account, transaction_history= None, daily_withdrawal_limit: int=25000, per_transaction_limit: int=10000, daily_transaction: int=0):
        self.account = account
        self.transaction_history = transaction_history or []
        self.daily_withdrawal_limit = daily_withdrawal_limit
        self.per_transaction_limit = per_transaction_limit
        self.daily_transaction = daily_transaction

    def pin_validation(self):
        while True:
            try:
                pin = int(input("Please enter your PIN: "))
                if pin == self.account.get_pin():
                    return True
                else:
                    print("The entered PIN is incorrect.")
                    self.account.failed_pin_attempts += 1
                    if self.account.failed_pin_attempts >= 3:  # Check if attempts exceed threshold
                        self.account.is_account_locked = True
                        print("Maximum attempts reached. Your account is locked.")
                        return False
                    continue
            except ValueError:
                print("Please enter a valid numeric input.")
                return False


    def deposit(self, amount: int):
        if self.pin_validation():
            self.account.add_balance(amount)
            self.daily_transaction += amount
            print(f"Transaction successful: {amount} has been deposited into your account.")
            self.transaction_history.append(f"Deposit: {amount} was successfully added to your account.")
        else:
            print("Transaction failed: Invalid PIN.")

    def withdraw(self, amount: int):
        if amount > 0:
            if amount <= self.per_transaction_limit:
                if amount <= self.daily_withdrawal_limit:
                    if amount <= self.account.get_balance():
                        if self.pin_validation():
                            self.account.deduct_balance(amount)
                            self.daily_transaction += amount
                            print(f"Transaction successful: {amount} has been withdrawn.")
                            self.transaction_history.append(f"Withdrawal: {amount} was withdrawn.")
                        else:
                            print("Transaction failed: Incorrect PIN.")
                    else:
                        print("Transaction failed: Insufficient funds.")
                else:
                    print("Transaction failed: Amount exceeds daily withdrawal limit.")
            else:
                print("Transaction failed: Amount exceeds per transaction limit.")
        else:
            print("Transaction failed: Withdrawal amount must be at least 1.")

    def transfer(self, amount: int, account_no: int):
        if amount > 0:
            if amount <= self.daily_withdrawal_limit:
                if amount <= self.account.get_balance():
                    if self.pin_validation():
                        self.account.deduct_balance(amount)
                        self.daily_transaction += amount
                        print(f"Transaction successful: {amount} has been transferred to account {account_no}.")
                        self.transaction_history.append(f"Transfer: {amount} was successfully transferred to account {account_no}.")
                    else:
                        print("Transaction failed: Invalid PIN.")
                else:
                    print("Transaction failed: Insufficient balance for this transfer.")
            else:
                print("Transaction failed: Amount exceeds daily withdrawal limit.")
        else:
            print("Transaction failed: The transfer amount must be at least 1.")

    def check_balance(self):
        if self.pin_validation():
            print(f"Your current balance is: {self.account.get_balance()}")
        else:
            print("Access denied: Invalid PIN.")

    def get_transaction_history(self):
        if self.transaction_history:
            print("Transaction History:")
            for history in self.transaction_history:
                print(history)
        else:
            print("No transactions found in the history.")
