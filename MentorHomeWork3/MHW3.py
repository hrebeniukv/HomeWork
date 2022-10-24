import uuid
from datetime import date
import art


class Bank_account:
    deposit: int = 0

    def __init__(self, name: str, deposit_amount: int or float, percent: int):
        self.name = name
        self.deposit_amount = deposit_amount
        self.__percent = percent
        self.__open_deposit_sate = date.today()
        self.__account_number = uuid.uuid4()
        Bank_account.increase_class_deposit(self.deposit_amount)

    def __str__(self):
        return f"Баланс Вашого рахунку становить {self.deposit_amount}грн.Також до вашого основного рахунку " \
               f"нараховується {self.__percent}% річних."

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, new_percent):
        self.__percent = new_percent

    @classmethod
    def increase_class_deposit(cls, amount):
        Bank_account.deposit += amount

    def increase_deposit(self, amount):
        self.deposit_amount += amount
        Bank_account.increase_class_deposit(amount)

    @classmethod
    def decrease_class_deposit(cls, amount):
        Bank_account.deposit -= amount

    def decrease_deposit(self, amount):
        if self.deposit_amount - amount >= 0:
            self.deposit_amount -= amount
        else:
            self.deposit_amount = 0
        Bank_account.decrease_class_deposit(amount)

    def __del__(self):
        print(
            f"Рахунок номер {self.__account_number} закрито,сумма до повернена клієнту {self.name} становить {self.deposit_amount}грн.")
        Bank_account.decrease_class_deposit(self.deposit_amount)

    def transfer(self, other_account, transfer_amount):
        if self.deposit_amount > transfer_amount:
            self.deposit_amount -= transfer_amount
            other_account.deposit_amount += transfer_amount
        else:
            other_account.deposit_amount += self.deposit
            self.deposit_amount = 0

    @staticmethod
    def bank_tagline():
        tagline = art.tprint("Time it is money", "00000")
        print(tagline)


James = Bank_account('James', 9000, 7)
Braian = Bank_account('Braian', 27000, 8)
James.percent = 8
Braian.decrease_deposit(29000)
James.increase_deposit(10000)
James.transfer(Braian, 8000)
