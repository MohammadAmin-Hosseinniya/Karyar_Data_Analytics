class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest of ${interest}. New balance: ${self.balance}")

# Example usage:
if __name__ == "__main__":
    account1 = Account(1001, "Alice")
    account1.deposit(1000)
    account1.withdraw(200)

    print("____________________")
    print("____________________\n")

    savings_account1 = SavingsAccount(2001, "Bob", 5000, 0.05)
    savings_account1.deposit(1000)
    savings_account1.add_interest()

