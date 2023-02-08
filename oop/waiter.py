import datetime
from oop.restaurant_worker import RestaurantWorker


class Waiter(RestaurantWorker):
    def __init__(self, name: str, date_of_employment: tuple, hour_salary: int | float,
                 tips: int | float, work_hour_per_month: int):
        super().__init__(name, date_of_employment, hour_salary, work_hour_per_month)
        self.__tips = tips

    def __str__(self):
        return f" My name is {self.name}, I have been work in this restaurant for {self.experience()} month as waiter."

    def do_work(self):
        print("Hi, I am waiter, I going to serve food for you")

    def experience(self):
        experience = datetime.date.today() - self._date_of_employment
        return experience.days // 30

    def change_salary(self, value):
        self._hour_salary = self._hour_salary + value

    @property
    def work_hour_per_month(self):
        return self._work_hour_per_month

    @work_hour_per_month.setter
    def work_hour_per_month(self, hours):
        self._work_hour_per_month = hours

    @property
    def month_salary(self):
        month_salary = self._work_hour_per_month * self._hour_salary + self.__tips
        return month_salary


waiter = Waiter("Pawel", (2019, 11, 23), 34, 200, 144)
print(waiter.experience())
