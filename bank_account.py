class AccountDB:
    def __init__(self) -> None:
        self.account_database = []
        
    def insert(self, account):
        index = self.search(account.account_num)
        if index == None:
            self.account_database.append(account)
        else:
            print(account, "Duplicated account; nothing to be insert")

    def search(self, account_num):
        for i in range(len(self.account_database)):
            if self.account_database[i].account_num == account_num:
                return i
        return None
    
    def search_public(self, account_num):
        for i in self.account_database:
            if i.account_num == account_num:
                return i
        return None
    
    def delete(self, account_num):
        for i in self.account_database:
            if i.account_num == account_num:
                self.account_database.remove(i)
    
    def __str__(self):
        s = ''
        for i in self.account_database:
            s += str(i) + '\n'
        return s
    
    
class Account:
    def __init__(self, num, type, account_name, balance):
        self.account_num = num
        self.type = type
        self.account_name = account_name
        self.balance = balance
        
    def deposit(self, amount):
        if not isinstance(amount, (int,float)):
            raise TypeError("Enter NUMBERS")
        if amount <= 0:
            raise ValueError("Value can't be less than or equal to 0")
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        
    def __str__(self) -> str:
        return f"{self.account_num}, {self.account_name}, {self.type}, balance = {self.balance} Baht"
    
    
account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)
account4 = Account("0004", "saving", "David Wood", 4000)
account5 = Account("0004", "saving", "David Wood", 4000)
my_account_DB = AccountDB()
my_account_DB.insert(account1)
my_account_DB.insert(account2)
my_account_DB.insert(account3)
my_account_DB.insert(account4)
my_account_DB.insert(account5)
print(my_account_DB)
my_account_DB.search_public("0003").deposit(50)
print(my_account_DB)
my_account_DB.search_public("0003").withdraw(100)
print(my_account_DB)
my_account_DB.delete("0001")
print(my_account_DB)