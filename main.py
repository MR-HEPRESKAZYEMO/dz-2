# Завдання 1

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Рахунок поповнено на {amount}. Новий баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Знято {amount}. Залишок: {self.balance}")
        else:
            print("Недостатньо коштів на рахунку.")


account = BankAccount("UA123456789", 1000)

account.deposit(500)
account.withdraw(300)
account.withdraw(1500)



# Завдання 2

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"


car = Car("BMW", "M5", 2025)

print(car.get_info())