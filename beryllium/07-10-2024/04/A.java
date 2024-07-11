import java.util.ArrayList;
import java.util.List;

class BankAccount {

    private double balance = 0.0;

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && balance >= amount) {
            balance -= amount;
        }
    }

    public double getBalance() {
        return balance;
    }
}

class Bank {

    private List<BankAccount> accounts = new ArrayList<>();

    public int createAccount() {
        accounts.add(new BankAccount());
        return accounts.size() - 1; // Return the index of the newly created account
    }

    public void deposit(int accountNumber, double amount) {
        if (accountNumber >= 0 && accountNumber < accounts.size()) {
            accounts.get(accountNumber).deposit(amount);
        }
    }

    public void withdraw(int accountNumber, double amount) {
        if (accountNumber >= 0 && accountNumber < accounts.size()) {
            accounts.get(accountNumber).withdraw(amount);
        }
    }

    public double getBalance(int accountNumber) {
        if (accountNumber >= 0 && accountNumber < accounts.size()) {
            return accounts.get(accountNumber).getBalance();
        }
        return 0.0;
    }
}

public class A {

    public static void main(String[] args) {
        Bank bank = new Bank();
        int account1 = bank.createAccount();
        int account2 = bank.createAccount();

        bank.deposit(account1, 100.0);
        bank.deposit(account2, 50.0);

        bank.withdraw(account1, 50.0);

        System.out.println("Account 1 balance: " + bank.getBalance(account1));
        System.out.println("Account 2 balance: " + bank.getBalance(account2));
    }
}