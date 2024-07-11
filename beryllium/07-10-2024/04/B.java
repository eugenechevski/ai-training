import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class B {
    private List<Account> accounts = new ArrayList<>();

    public void createAccount(String name) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Invalid account name: Name cannot be empty.");
        }

        accounts.add(new Account(name));
        System.out.println("Account created for holder: " + name);
    }

    public void depositFunds(int accountNumber, double amount) {
        Account account = getAccount(accountNumber);
        if (account != null) {
            account.deposit(amount);
            System.out.println("Deposited $" + amount + ". Available balance: $" + account.getBalance());
        } else {
            System.out.println("Account not found.");
        }
    }
    public void withdrawFunds(int accountNumber, double amount) {
        Account account = getAccount(accountNumber);
        if (account != null) {
            if (account.withdraw(amount)) {
                System.out.println("Withdrawn $" + amount + ". Available balance: $" + account.getBalance());
            } else {
                System.out.println("Insufficient balance. Transaction failed.");
            }
        } else {
            System.out.println("Account not found.");
        }
    }

    public void checkBalance(int accountNumber) {
        Account account = getAccount(accountNumber);
        if (account != null) {
            System.out.println("Available Balance: $" + account.getBalance());
        } else {
            System.out.println("Account not found.");        
        }
    }
    
    private Account getAccount(int accountNumber) {
        for (Account account : accounts) {
            if (account.getAccountNumber() == accountNumber) {
                return account;
            }
        }
        return null;
    }
    
    public void displayAllAccounts() {
        System.out.println("\nAll Accounts:");
        for (Account account : accounts) {
            System.out.println("Account Number: " + account.getAccountNumber() + 
                                ", Holder Name: " + account.getAccountHolderName() + 
                                ", Balance: $" + account.getBalance());
        }
    }

    public static void main(String[] args) {
        B bank = new B();
        Scanner scanner = new Scanner(System.in);
        int option;

        do {
            System.out.println("\nMenu:");
            System.out.println("1. Create Account");
            System.out.println("2. Deposit Funds");
            System.out.println("3. Withdraw Funds");
            System.out.println("4. Check Balance");
            System.out.println("5. List All Accounts");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            option = scanner.nextInt();

            try {
                switch (option) {
                    case 1:
                        System.out.print("Enter account holder name: ");
                        String name = scanner.next();
                        bank.createAccount(name);
                        break;
                    case 2:
                        System.out.print("Enter account number: ");
                        int accountNumber = scanner.nextInt();
                        System.out.print("Enter deposit amount: ");
                        double amount = scanner.nextDouble();
                        bank.depositFunds(accountNumber, amount);
                        break;
                    case 3: 
                        System.out.print("Enter account number: ");
                        accountNumber = scanner.nextInt();                    
                        System.out.print("Enter withdrawal amount: ");
                        amount = scanner.nextDouble();
                        bank.withdrawFunds(accountNumber, amount);
                        break;
                    case 4:
                        System.out.print("Enter account number: ");
                        accountNumber = scanner.nextInt();
                        bank.checkBalance(accountNumber);
                        break;
                    case 5:
                        bank.displayAllAccounts();
                        break;
                    case 6:
                        System.out.println("Goodbye!");
                        break;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
            }
        } while (option != 6);
        scanner.close();
    } 
    private static class Account {
        private int accountNumber;
        private String accountHolderName;
        private double balance;

        public Account(String name) {
           this.accountHolderName = name;
           this.accountNumber =  (int) (Math.random() * 900000) + 100000;
        }

        public void deposit(double amount) {
            if (amount > 0) {
                balance += amount;
            }
        }

        public boolean withdraw(double amount) {
            if (amount > 0 && balance >= amount) {
                balance -= amount;
                return true;
            }
            return false;
        }
        public double getBalance() {
            return balance;
        }
        public int getAccountNumber() {
            return accountNumber;
        }
        public String getAccountHolderName() {
            return accountHolderName;
        }      
    }
}