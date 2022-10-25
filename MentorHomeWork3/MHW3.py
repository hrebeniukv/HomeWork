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
        """Return the value of private variable "__percent" """
        return self.__percent

    @percent.setter
    def percent(self, new_percent: int):
        """This function set the private variable "__percent" """
        self.__percent = new_percent

    @classmethod
    def increase_class_deposit(cls, amount: int or float):
        """Function gets the mandatory variable and increase the class variable on the value of the got variable"""
        Bank_account.deposit += amount

    def increase_deposit(self, amount: int or float):
        """Function gets the mandatory variable and increase the self variable on the value of the got variable
        also it triggers a class method for update the class variable"""
        self.deposit_amount += amount
        Bank_account.increase_class_deposit(amount)

    @classmethod
    def decrease_class_deposit(cls, amount: int or float):
        """Function gets the mandatory variable and decreases the class variable on the value of the got variable"""
        Bank_account.deposit -= amount

    def decrease_deposit(self, amount: int or float):
        """Function gets the mandatory variable and decreases the self variable on the value of the got variable
        also it triggers a class method for update the class variable"""
        if self.deposit_amount >= amount:
            self.deposit_amount -= amount
            Bank_account.decrease_class_deposit(amount)
        else:
            Bank_account.decrease_class_deposit(self.deposit_amount)
            self.deposit_amount = 0

    def __del__(self):
        """This function 'kill' the object of class and print inform message,
        also it triggers a class method for update the class variable"""
        print(f"Рахунок номер {self.__account_number} закрито,сумма до повернена клієнту {self.name} становить {self.deposit_amount}грн.")
        Bank_account.decrease_class_deposit(self.deposit_amount)

    def transfer(self, other_account, transfer_amount: int or float):
        """land money from self account to other_account, "transfer_amount" it is value of transfer """
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
Braian.decrease_deposit(1000000)
James.increase_deposit(10000)
James.transfer(Braian, 8000)

