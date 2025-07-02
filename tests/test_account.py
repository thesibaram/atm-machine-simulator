from datetime import datetime

class Account:

    def __init__(self, name: str, account_no: int, pin: int , balance = 0, account_type="Savings",
                 date_of_opening=None, status="Active", security_answer=None):
        self.name = name
        self.__account_no = account_no
        self.__pin = pin
        self.__balance = balance
        self.account_type = account_type
        self.date_of_opening = date_of_opening or datetime.now().strftime("%Y-%m-%d")
        self.status = status
        self.security_answer = security_answer or {}

    def __str__(self):
        return f"Name: {self.name}, Acc No: {self.__account_no}, Balance: ₹{self.__balance:.2f}"

    def get_pin(self):
        return self.__pin

    def get_balance(self):
        return self.__balance

    def get_acc_no(self):
        return self.__account_no

    def add_balance(self, amount: int):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            print("Amount should be at least 1")
            return False

    def deduct_balance(self, amount: int):
        if amount > 0:
            self.__balance -= amount
            return True
        else:
            print("Amount should be at least 1")
            return False

    def change_pin(self):
        try:
            current_pin = int(input("Please enter your current Personal Identification Number (PIN): "))
            if current_pin == self.get_pin():
                new_pin = int(input("Please enter your new Personal Identification Number (PIN): "))
                confirm_pin = int(input("Please re-enter your new Personal Identification Number (PIN) to confirm: "))
                if new_pin == confirm_pin:
                    self.__pin = new_pin
                    print("Your Personal Identification Number (PIN) has been successfully updated.")
                    return True
                else:
                    print("The entered Personal Identification Numbers (PINs) do not match. Please try again.")
                    return False
            else:
                print("The current Personal Identification Number (PIN) entered is incorrect.")
                return False
        except ValueError:
            print("An error occurred: Please enter a valid numeric Personal Identification Number (PIN).")
            return False

    def security_question(self):
        print("Please choose a security question:")
        security_questions = [
            "What is your pet's name?",
            "What is your birth city?",
            "What is your favorite food?"
        ]

        for n, q in enumerate(security_questions, start=1):
            print(f"{n}. {q}")

        try:
            option = int(input("Please select an option (1 to 3): "))
            if 1 <= option <= len(security_questions):
                selected_question = security_questions[option - 1]
                answer = input(f"Answer to '{selected_question}': ")
                if answer:
                    self.security_answers = {selected_question: answer}
                else:
                    self.security_answers = {selected_question: None}
            else:
                print("Invalid option selected.")
        except ValueError:
            print("Please enter a valid number.")

    def security_question_validation(self):
        for question, answer in self.security_answers.items():
            if answer is not None:
                print(question)
                try:
                    ans = input("Please enter the answer to the question: ")
                    if ans == answer:
                        return True
                    else:
                        print("The answer provided is incorrect. Please try again.")
                        return False
                except Exception as e:
                    print(f"An error occurred: {e}")
                    return False

    def forget_pin(self):
        try:
            acc_no = int(input("Please enter your Account Number: "))
            reg_name = input("Please enter your Registered Name: ")
            if acc_no == self.get_acc_no() and reg_name == self.name:
                if self.security_question_validation():
                    new_pin = int(input("Please enter your new Personal Identification Number (PIN): "))
                    confirm_pin = int(input("Please re-enter your new Personal Identification Number (PIN) to confirm: "))
                    if new_pin == confirm_pin:
                        self.__pin = new_pin
                        print("Your Personal Identification Number (PIN) has been successfully reset.")
                        return True
                    else:
                        print("The entered Personal Identification Numbers (PINs) do not match. Please try again.")
                        return False
                else:
                    print("Security question validation failed.")
                    return False
            else:
                print("The details provided do not match our records.")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False


