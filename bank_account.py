class AccountDB:
    def __init__(self) -> None:
        self.account_database = []
        
    def insert(self, account):
        index = self.search(account.account_num)
        if index == None:
            self.account_database.append(account)

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
    
    def __str__(self):
        s = ''
        for i in self.account_database:
            s += str(i) + '\n'
        return s
    
    
class Account:
    def __init__(self, num, type, account_name, balance) -> None:
        self.account_num = num
        self.type = type
        self.account_name = account_name
        self.balance = balance
        
    def deposit(self, amount):
        if not isinstance(amount, (int,float)):
            raise TypeError('Enter NUMBERS')
        if amount < 0:
            raise ValueError('Are u sane?')
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        
    def __str__(self) -> str:
        return f"{self.account_num}, {self.account_name}, {self.type}, balance = {self.balance} Baht"
    
    
a1 = Account("0000", "saving", "David Patterson", 1000)
a2 = Account("0001", "checking", "John Hennessy", 2000)
a3 = Account("0003", "saving", "Mark Hill", 3000)
a4 = Account("0004", "saving", "David Wood", 4000)

db = AccountDB()
db.insert(a1)
db.insert(a2)
db.insert(a3)
db.insert(a4)
print(db)
db.search_public("0003").deposit(50)
print(db)