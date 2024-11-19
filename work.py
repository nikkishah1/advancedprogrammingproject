
class BankAccount:
    def __init__(self, iban, name, balance = 0):
        if not isinstance(iban, str) or not isinstance(name, str):
            raise ValueError
        if not isinstance(balance, (int, float)):
            raise ValueError
        if balance < 0:
            raise ValueError
        self.iban = iban
        self.name = name
        self.balance = balance

        
    def deposit(self, amount):

        if isinstance(amount, (int, float)) == False:
            raise ValueError
        if amount < 0 :
            raise ValueError 
        else:
            self.balance = self.balance + amount
            return(amount)

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) == False:
            raise ValueError
        if amount > self.balance or amount < 0:
            raise ValueError
        else:
            self.balance = self.balance - amount
            return(amount)

        
    def get_balance(self):
        return(self.balance)
    def get_iban(self):
        return(self.iban)
    def get_name(self):
            return(self.name)
    def transfer(self, destination_account, amount):

        if not isinstance(destination_account, BankAccount):
            raise ValueError
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError
        if amount > self.balance:
            raise ValueError
        else:
            self.withdraw(amount)
            destination_account.deposit(amount)
            return(amount)



class MinimumBalanceAccount(BankAccount):
    debug = False 

    def __init__(self, iban, name, minimum_balance = 100, initial_deposit = 100): 
            if isinstance(initial_deposit, (int, float)) == False:
                raise ValueError
            if isinstance(minimum_balance, (int, float)) == False:
                raise ValueError
            if minimum_balance > initial_deposit or minimum_balance < 0:
                raise ValueError
            if minimum_balance <= initial_deposit and minimum_balance > 0: 
                super().__init__(iban, name, initial_deposit)
                self.minimum_balance = minimum_balance
                self.balance = initial_deposit
            else: 
                raise ValueError
    def set_minimum_balance(self, amount):
            if amount > self.balance or amount < 0:
                raise ValueError
            else:
                self.minimum_balance = amount
                return(amount)
    def get_minimum_balance(self):
            return self.minimum_balance

    def deposit(self, amount):
            if isinstance(amount, (int, float)) == False:
                raise ValueError
            if amount < self.balance - self.minimum_balance or amount < 0:
                raise ValueError
            else:
                self.balance = self.balance + amount
                return(amount)
    

    def withdraw(self, amount):
            if isinstance(amount, (int, float)) == False:
                raise ValueError
            if amount > self.balance - self.minimum_balance or amount < 0:
                raise ValueError
            else:
                self.balance = self.balance - amount
                return(amount)
    def transfer(self, destination_account, amount):
        if not isinstance(destination_account, BankAccount):
            raise ValueError
        if isinstance(amount, (int, float)) == False or amount < 0:
            raise ValueError
        if amount > self.balance - self.minimum_balance:
            raise ValueError
        else:
            self.withdraw(amount)
            destination_account.deposit(amount)
            return(amount)
