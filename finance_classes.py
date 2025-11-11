class User:
    def __init__(self, login, name, budget):
        self.login = login
        self.name = name
        self.bal = float(budget)
        self.spent = 0
        self.income = 0
    
    def add_expense(self, amount):
        if amount > self.bal:
            return False
        self.spent += amount
        self.bal -= amount
        return True
    
    def add_income(self, amount):
        self.bal += amount
        self.income += amount
        return True
    
    def get_info(self):
        return f"{self.name} | balance:{self.bal}₸ | spent:{self.spent}₸ | income:{self.income}₸"
    
    def __str__(self):
        return self.get_info()

class FamilyAccount:
    def __init__(self):
        self.deposit = 0
    
    def add_funds(self, amount, user):
        if amount > user.bal:
            return False
        self.deposit += amount
        user.bal -= amount
        return True
    
    def get_total(self):
        return self.deposit

class FinanceManager:
    def __init__(self):
        self.users = []
        self.family_account = FamilyAccount()
    
    def add_user(self, login, name, budget):
        user = User(login, name, budget)
        self.users.append(user)
        return user
    
    def find_user(self, name):
        for user in self.users:
            if user.name.lower() == name.lower():
                return user
        return None
    
    def delete_user(self, name):
        user = self.find_user(name)
        if user:
            self.users.remove(user)
            return True
        return False
    
    def show_all_users(self):
        if not self.users:
            print("No users found")
            return
        for i, user in enumerate(self.users):
            print(f"{i+1}. {user}")

class Admin(User):  # Пример наследования
    def __init__(self, login, name, budget, admin_level=1):
        super().__init__(login, name, budget)
        self.admin_level = admin_level
    
    def get_admin_info(self):
        return f"Admin {self.name} (Level {self.admin_level}) - {self.get_info()}"
