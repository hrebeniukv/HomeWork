import random
from abc import ABC, abstractmethod
from faker import Faker
from random import randint, choice


class SchoolEmployee(ABC):
    employee_list = []

    def __init__(self, name: str, salary: int | float):
        self.name = name
        self.salary = salary
        SchoolEmployee.employee_list.append(self)

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

    def __init__(self, school_name: str, manager: Teacher, employee_list: list):
        self.school_name = school_name
        self.manager = manager
        self.teacher_list = [employee for employee in employee_list if
                             isinstance(employee, Teacher) and employee != self.manager]
        self.tech_staff_list = [employee for employee in employee_list if isinstance(employee, TechnicalStaff)]
        self.__employee_list = employee_list

    @property
    def total_employees_salary(self) -> int | float:
        """Function count and receive the total salary of school employee"""
        return sum([employee.__dict__['salary'] for employee in self.__employee_list])

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
        return [employee.__dict__['name'] for employee in self.__employee_list]


teachers = [Teacher(Faker().name(), random.randint(20000, 50000)) for i in range(10)]
staff = [TechnicalStaff(Faker().name(), random.randint(20000, 50000)) for i in range(10)]
maneger = Teacher(Faker().name(), random.randint(20000, 50000))
school1 = School("Barvinok", maneger, SchoolEmployee.employee_list)
print(*school1.show_teachers_list(), sep="\n")
print(school1.total_employees_salary)
school1.set_new_manager()
