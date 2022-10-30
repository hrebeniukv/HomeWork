from abc import abstractmethod
import random


class SchoolEmployees:
    total_salary = 0

    def __init__(self, name: str, last_name: str, salary: int):
        self.name = name
        self.last_name = last_name
        self.salary = salary
        SchoolEmployees.total_teachers_salary(self.salary)
        if type(self) is Teachers:
            Teachers.teachers_list.append(f"{self.name} {self.last_name}")
        elif type(self) is Staff:
            Staff.staff_list.append(f"{self.name} {self.last_name}")

    @abstractmethod
    def __str__(self):
        return "Not Implemented Error"

    @classmethod
    def total_teachers_salary(cls, employee_salary):
        cls.total_salary += employee_salary


class Staff(SchoolEmployees):
    staff_list = []

    def __str__(self):
        return f"New employee of technical staff is {self.name} {self.last_name} with salary {self.salary}UAH"


class Teachers(SchoolEmployees):
    teachers_list = []

    @classmethod
    def add_teacher_to_lis(cls, teacher: str):
        cls.teachers_list.append(teacher)

    @classmethod
    def remove_teacher_from_lis(cls, teacher: str):
        cls.teachers_list.remove(teacher)

    def __str__(self):
        return f"New employee of technical staff is {self.name} {self.last_name} with salary {self.salary}UAH"


class School:

    def __init__(self, school_name: str, director: str, teachers_list: list, staff_list: list, total_month_salary: int):
        self.school_name = school_name
        self.teachers_list = teachers_list
        self.staff_list = staff_list
        if director in self.teachers_list:
            Teachers.remove_teacher_from_lis(director)
            self.director = director
        else:
            self.director = random.choice(self.teachers_list)
            Teachers.remove_teacher_from_lis(self.director)
        self.__total_month_salary = total_month_salary

    def change_director(self, director_full_name: str):
        Teachers.add_teacher_to_lis(self.director)
        self.director = director_full_name
        Teachers.remove_teacher_from_lis(self.director)

    def new_teacher(self, name: str, last_name: str, salary: int):
        Teachers(name, last_name, salary)
        self.__total_month_salary += salary

    @property
    def get_total_salary(self):
        return self.__total_month_salary


test_name = ["Jon", "Kris", "Ostin", "Bart"]
test_last_name = ["Ossborne", "Engel", "Pouwer", "Simson"]
test_salary = [18000, 25000, 13000, 27000]
teacher1 = Teachers("Jon", "Ossborne", 18000)
teacher2 = Teachers("Kris", "Engel", 12000)
teacher3 = Teachers("Ostin", "Pouwer", 24000)
teacher4 = Teachers("Bart", "Simson", 32000)

staff1 = Staff("Jon", "Engel", 13000)
staff2 = Staff("Kris", "Pouwer", 7200)
staff3 = Staff("Ostin", "Simson", 14000)
staff4 = Staff("Bart", "Ossborne", 18000)

sk1 = School("Barvinok", "Bart Ossborne", Teachers.teachers_list, Staff.staff_list, SchoolEmployees.total_salary)
print(*sk1.teachers_list, sep="\n")
print(f"The total salary of workers per month is equal to: {sk1.get_total_salary}UAH")
sk1.new_teacher("Rasel", "Joui", 27000)
sk1.change_director("Bart Simson")
print(*sk1.teachers_list, sep="\n")
