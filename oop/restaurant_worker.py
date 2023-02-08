import datetime
from abc import ABC, abstractmethod


class RestaurantWorker(ABC):

    def __init__(self, name: str, date_of_employment: tuple, hour_salary: int | float, work_hour_per_month: int):
        self.name = name
        self._date_of_employment = datetime.date(year=date_of_employment[0], month=date_of_employment[1],
                                                 day=date_of_employment[2])
        self._hour_salary = hour_salary
        self._work_hour_per_month = work_hour_per_month

    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def experience(self):
        pass

    @abstractmethod
    def change_salary(self, value):
        pass

    @abstractmethod
    def month_salary(self):
        pass
