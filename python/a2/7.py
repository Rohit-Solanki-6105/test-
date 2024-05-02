'''
7. Creating a Bank Account Class with Inheritance
    >   Define a base class Account with attributes like account_no (string) and balance 
        (float). Implement constructor method in Account to initialize these attributes.
    >   Create a subclass BankAccount that inherits from Account. 
    >   Add a method called deposit(amount) to BankAccount to add funds to the balance.
    >   Optionally, you can add a withdraw(amount) method that subtracts funds from the 
        balance while considering overdraft protection (if applicable).
'''

class Account:
    def __init__(self, account_no, balance=0.0):
        self.account_no = account_no
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_no}, Balance: Rs.{self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount:.2f} into account {self.account_no}. New balance: Rs.{self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew Rs.{amount:.2f} from account {self.account_no}. New balance: Rs.{self.balance:.2f}")
            else:
                print("Insufficient funds. Withdrawal amount exceeds available balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")


class BankAccount(Account):
    def __init__(self, account_no, balance=0.0):
        super().__init__(account_no, balance)

    # Override the withdraw method to include overdraft protection
    def withdraw(self, amount):
        overdraft_limit = 100.0  # Define overdraft protection limit

        if amount > 0:
            if self.balance + overdraft_limit >= amount:
                self.balance -= amount
                print(f"Withdrew Rs.{amount:.2f} from account {self.account_no}. New balance: Rs.{self.balance:.2f}")
            else:
                print("Withdrawal amount exceeds available balance including overdraft protection.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")


bank_account = BankAccount("123456789", 100.0)

print(bank_account)

bank_account.deposit(500.0)

bank_account.withdraw(300.0)

bank_account.withdraw(500.0)

bank_account.withdraw(-50.0)

'''
Account Number: 123456789, Balance: Rs.100.00
Deposited Rs.500.00 into account 123456789. New balance: Rs.600.00
Withdrew Rs.300.00 from account 123456789. New balance: Rs.300.00
Withdrawal amount exceeds available balance including overdraft protection.
Invalid withdrawal amount. Please enter a positive value.
'''