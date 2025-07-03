class AtmMachine:
    def menu(self):
        menu_list = [
            "Make a Deposit",
            "Make a Withdrawal",
            "Transfer Funds",
            "Check Account Balance",
            "View Transaction History",
            "Change PIN",
            "Exit"
        ]
        print("Please select an option between(1 to 7):")
        for no, item in enumerate(menu_list, start=1):
            print(f"{no}. {item}")

    def get_menu_list(self):
        return self.menu

