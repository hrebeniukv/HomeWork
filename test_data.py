# # # #
# # def print_result(print_template):
# #     def dec(func):
# #         def wrapper(*args, **kwargs):
# #             result = func(*args, **kwargs)
# #             print(f"{print_template} is: {result} ")
# #             return result
# #
# #         return wrapper
# #
# #     return dec
# #
# #
# # #
# # #
# # # #
# # # def checking_on_number():
# # #     def wrapper(*args, **kwargs):
# # #
# # #         try:
# # #             for i in args:
# # #                 float(i)
# # #
# # #             for y in kwargs.values():
# # #                 float(y)
# # #             return map(float, (args)), map(float, (kwargs))
# # #         except ValueError:
# # #             print("Entered data is not number")
# # #             return "data is not a number"
# # #
# # #     return wrapper
# # #
# # #
# # # # # 1.напишіть функцію, яка перевірить, чи передане їй число є парним чи непарним (повертає True False)
# # # #
# # # @print_result('Result of checking the number')
# # # # @checking_on_number
# # # def cheking_nubmer(test_number) -> bool:
# # #     result = True if float(test_number) % 2 == 0 else False
# # #     return result
# # #
# # #
# # # cheking_nubmer(input("Please, enter the number: "))
# # #
# # #
# # # #
# # # #
# # # # assert type(cheking_nubmer(2)) is bool
# # # # # assert
# # # # # assert
# # # # # assert
# # # # # assert
# # # #
# # # #
# 2. напишіть функцію. яка приймає стрічку, і визначає, чи дана стрічка відповідає результатам роботи методу capitalize()
# (перший символ є верхнім регістром, а решта – нижнім.) (повертає True False)
#
# @print_result('Result of checking the string')
# def checking_string(test_string: str) -> bool:
#     return True if test_string == test_string.capitalize() else False
#
#
# checking_string(input("Please, enter some text: "))
# # # #
# # # #
# # # # # # assert
# # # # # # assert
# # # # # # assert
# # # # # # assert
# # # # # # assert
# # # #
# # # #
# # # #
# # # #
# # # #
# # #
# # # def changing_to_number(func):
# # #     def wrapper(string_number):
# # #
# # #         try:
# # #             test_number = float(string_number)
# # #             return func(test_number)
# # #         except ValueError:
# # #             # print("Entered data is not number")
# # #             return "data is not a number"
# # #
# # #     return wrapper
# #
# # @print_result('Result of checking the number to parity')
# # def cheking_nubmer(test_number) -> bool:
# #     try:
# #         return True if float(test_number) % 2 == 0 else False
# #     except:
# #         return False
# #
# #
# #
# #
# #
# #
# # assert cheking_nubmer(10) is True
# # assert cheking_nubmer(9999999) is False
# # assert cheking_nubmer('10.00') is True
# # assert cheking_nubmer('not a number') is False
# # assert cheking_nubmer(10.2) is False
# # assert cheking_nubmer(-10) is True
# # assert cheking_nubmer(0) is True
# # assert type(cheking_nubmer(10)) is bool
#
#
# # print('10'.capitalize())
#
#
# def d(test_string='!Ttttt'):
#     return True if test_string[0].isalpha() and test_string == test_string.capitalize() else False
#
#
# print(d())
import random

from faker import Faker

# print(Faker().name().split()[0])


# print(fake.name().split()[1])
class new:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    pass


news = [new(Faker().name().split()[0], Faker().name().split()[1], random.randint(20000, 50000)) for i in range(10)]
print()
