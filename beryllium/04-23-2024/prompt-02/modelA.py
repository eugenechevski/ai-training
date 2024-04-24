import datetime

class BankAccount:
    next_account_number = 1000

    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._add_transaction(amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        self._add_transaction(-amount)

    def _add_transaction(self, amount):
        self.transaction_history.append(
            {
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "amount": amount,
                "balance": self.balance,
            }
        )

    def get_balance(self):
        return self.balance

    def get_account_details(self):
        return (
            f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.name}\n"
            f"Balance: ${self.get_balance():.2f}\n"
        )
        
    def get_transaction_history(self):
        print(f"Transaction History for Account Number: {self.account_number}")
        print("--------------------------")
        for transaction in self.transaction_history:
            print(f"{transaction['date']}: ${transaction['amount']:+.2f} -> {transaction['balance']:.2f}")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, initial_balance=0):
        if name in self.accounts:
            print("Account already exists.")
        else:
            new_account = BankAccount(name, initial_balance)
            self.accounts[name] = new_account
            print(f"Account created for {name}.")

    def deposit_funds(self, name, amount):
        account = self.accounts.get(name)
        if account:
            account.deposit(amount)
            print(f"${amount} deposited to {name}'s account. Available Balance: ${account.get_balance():.2f}")
        else:
            print("Account not found.")

    def withdraw_funds(self, name, amount):
        account = self.accounts.get(name)
        if account:
            try:
                account.withdraw(amount)
                print(f"${amount} withdrawn from {name}'s account. Available Balance: ${account.get_balance():.2f}")
            except ValueError as e:
                print(e)
        else:
            print("Account not found.")

    def transfer_funds(self, from_name, to_name, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
        else:
            from_account = self.accounts.get(from_name)
            to_account = self.accounts.get(to_name)
            if from_account and to_account:
                try:
                    from_account.withdraw(amount)
                    to_account.deposit(amount)
                    print(f"${amount} transferred from {from_name}'s account to {to_name}'s account.")
                    print(f"Available Balance in {from_name}'s account: ${from_account.get_balance():.2f}")
                    print(f"Available Balance in {to_name}'s account: ${to_account.get_balance():.2f}")
                except ValueError as e:
                    print(e)
            else:
                print("One or both accounts not found.")

    def list_all_accounts(self):
        print("--- Accounts List ---")
        for name, account in self.accounts.items():
            print(f"{name}: Account Number - {account.account_number}")

    def view_account_details(self, name):
        account = self.accounts.get(name)
        if account:
            print(account.get_account_details())
            account.get_transaction_history()
        else:
            print("Account not found.")

    def exit_system(self):
        print("Goodbye!")        


def main():
    bank = BankSystem()
    user_input = ""

    while user_input != "exit":
        print(
            """
            Welcome to ABC Bank!
            Please choose an option:
            1: Add a new account
            2: Deposit funds
            3: Withdraw funds
            4: Transfer funds
            5: List all accounts
            6: View account details
            7: Exit
            """
        )
        user_input = input("Enter your choice: ").lower()
        if user_input == "1":
            name = input("Enter the account holder's name: ")
            balance = float(input("Enter the initial balance (optional): ") or 0)
            bank.add_account(name, balance)
        elif user_input == "2":
            name = input("Enter account holder's name: ")
            amount = float(input("Enter the deposit amount: "))
            bank.deposit_funds(name, amount)
        elif user_input == "3":
            name = input("Enter account holder's name: ")
            amount = float(input("Enter the withdrawal amount: "))
            bank.withdraw_funds(name, amount)
        elif user_input == "4":
            from_name = input("Enter the sender's account holder name: ")
            to_name = input("Enter the recipient's account holder name: ")
            amount = float(input("Enter the transfer amount: "))
            bank.transfer_funds(from_name, to_name, amount)
        elif user_input == "5":
            bank.list_all_accounts()
        elif user_input == "6":
            name = input("Enter account holder's name to view details: ")
            bank.view_account_details(name)  
        elif user_input != "exit":
            print("Invalid choice. Please try again.")

    bank.exit_system()


if __name__ == "__main__":
    main()