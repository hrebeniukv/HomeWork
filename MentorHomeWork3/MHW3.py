import uuid
from datetime import date


class Bank_account:
    deposit: int = 0

    def __init__(self, name, deposit_amount, percent_increase):
        self.name = name
        self.deposit_amount = deposit_amount
        self.__percent_increase = percent_increase
        self.__open_deposit_sate = date.today()
        self.__account_number = uuid.uuid4()

    def __str__(self):
        return f"Баланс Вашого рахунку становить {Bank_account.deposit}грн.Також до вашого основного рахунку " \
               f"нараховується {self.__percent_increase}% річних. "

    def __del__(cls):
