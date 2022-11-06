import random
from abc import ABC, abstractmethod
from faker import Faker
from random import randint, choice


class SchoolEmployee(ABC):

    def __init__(self, name: str, salary: int | float):
        self.name: str = name
        self.salary: int | float = salary

    @abstractmethod
    def __str__(self):
        pass


class Teacher(SchoolEmployee):

    def __str__(self) -> str:
        return f"The {self.name} is a teacher with salary {self.salary}UAH."


class TechnicalStaff(SchoolEmployee):

    def __str__(self) -> str:
        return f"The {self.name} is a worker of technical staff with salary {self.salary}UAH."


class School:

    def __init__(self, school_name: str, manager: Teacher, teacher_number: int, staff_number: int):
        self.school_name: str = school_name
        self.manager: Teacher = manager
        self.teacher_list: list = [Teacher(Faker().name(), random.randint(20000, 50000)) for i in range(teacher_number)]
        self.tech_staff_list: list = [TechnicalStaff(Faker().name(), random.randint(20000, 50000)) for i in
                                      range(staff_number)]

    @property
    def total_employees_salary(self) -> int | float:
        """Function count and receive the total salary of school employee"""
        all_employees = [self.manager] + self.teacher_list + self.tech_staff_list
        total_salary = sum([employee.__dict__['salary'] for employee in all_employees])
        return total_salary

    def new_teacher(self, teacher: Teacher):
        """Function use for add new teacher.
        teacher: mandatory position argument, object of Teacher class
        """
        self.teacher_list.append(teacher)

    def set_new_manager(self):
        """Function random choose the manager from the teacher list. After chose, the object will remove from the
          teacher list. The current manager will add to the list of teachers"""
        new_manager = random.choice(self.teacher_list)
        self.teacher_list.remove(new_manager)
        self.teacher_list.append(self.manager)
        self.manager = new_manager

    def show_teachers_list(self) -> list:
        """Function return the list on teachers"""
        return [employee.__dict__['name'] for employee in self.teacher_list]


school1 = School("Barvinok", Teacher(Faker().name(), random.randint(20000, 50000)), 12, 10)
print(*school1.show_teachers_list(), sep="\n")
print(school1.total_employees_salary)
school1.set_new_manager()

school2 = School("Barvinok3", Teacher(Faker().name(), random.randint(30000, 60000)), 5, 6)
print(*school2.show_teachers_list(), sep="\n")
print(school2.total_employees_salary)
school2.set_new_manager()
