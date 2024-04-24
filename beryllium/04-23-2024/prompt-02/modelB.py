class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
       self.balance += amount
       return self.balance

    def withdraw(self, amount):
       if amount > self.balance:
           print("Insufficient balance.")
           return self.balance
       else:
           self.balance -= amount
           return self.balance

    def __str__(self):
       return f"Account owner: {self.owner}, Balance: {self.balance}"

class Transaction:
   def __init__(self, sender, receiver, amount):
       self.sender = sender
       self.receiver = receiver
       self.amount = amount

   def perform_transaction(self):
       if self.sender.balance < self.amount:
           print("Insufficient balance.")
       else:
           self.sender.withdraw(self.amount)
           self.receiver.deposit(self.amount)
           print(f"Transaction successful. {self.amount} transferred from {self.sender.owner}'s account to {self.receiver.owner}'s account.")

def main():
   accounts = {}

   while True:
       print("\nMenu:")
       print("1. Add a new account")
       print("2. Update account balance")
       print("3. Transfer money")
       print("4. View all accounts")
       print("5. Exit")
       choice = int(input("Enter your choice: "))

       if choice == 1:
           name = input("Enter account owner's name: ")
           balance = float(input("Enter initial balance: "))
           accounts[name] = Account(name, balance)
           print(f"Account for {name} has been added.")

       elif choice == 2:
           name = input("Enter account owner's name: ")
           if name not in accounts:
               print("Account not found.")
           else:
               amount = float(input("Enter the amount to update the balance by: "))
               accounts[name].deposit(amount)
               print(f"Updated balance for {name} is {accounts[name].balance}.")

       elif choice == 3:
           sender_name = input("Enter sender's name: ")
           receiver_name = input("Enter receiver's name: ")
           amount = float(input("Enter the amount to transfer: "))

           if sender_name not in accounts or receiver_name not in accounts:
               print("One or both accounts not found.")
           else:
               t = Transaction(accounts[sender_name], accounts[receiver_name], amount)
               t.perform_transaction()

       elif choice == 4:
           for name, account in accounts.items():
               print(account)

       elif choice == 5:
           break

       else:
           print("Invalid choice.")

main()