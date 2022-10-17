# #
def print_result(print_template):
    def dec(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"{print_template} is: {result} ")
            return result

        return wrapper

    return dec


# 1.напишіть функцію, яка перевірить, чи передане їй число є парним чи непарним (повертає True False)


@print_result('Result of checking the number to parity')
def cheking_nubmer(test_number) -> bool:
    '''
    This function check if number is parity. https://en.wikipedia.org/wiki/Parity_(mathematics)
    :param test_number: mandatory argument which should be number
    :return: Return True if number is parity or False if number isn't parity
    '''
    try:
        return True if float(test_number) % 2 == 0 else False
    except:
        return False


assert cheking_nubmer(10) is True
assert cheking_nubmer('10.00') is True
assert cheking_nubmer(-10) is True
assert cheking_nubmer(0) is True
assert type(cheking_nubmer(10)) is bool
assert cheking_nubmer(9999999) is False
assert cheking_nubmer(10.2) is False
assert cheking_nubmer('not a number') is False
assert cheking_nubmer([10, 15]) is False
assert cheking_nubmer(('Test', 10)) is False
assert cheking_nubmer({'Test', 10}) is False
assert cheking_nubmer({'Test': 10, 10: "Test"}) is False

# cheking_nubmer(input("Please, enter the number: "))


# 2. напишіть функцію. яка приймає стрічку, і визначає, чи дана стрічка відповідає результатам роботи методу capitalize()
# (перший символ є верхнім регістром, а решта – нижнім.) (повертає True False)

@print_result('Result of checking the string')
def checking_string(test_string: str) -> bool:
    '''
    This function check if the text is in correct format.
    :param test_string: mandatory position argument
    :return: function return the "True" if text match to capitalize format or False if text doesn't match.
    '''
    try:
        test_string = str(test_string)
        return True if test_string[0].isalpha() and test_string == test_string.capitalize() else False
    except:
        return False
        # print('Something was wrong')


assert type(checking_string('Some text')) is bool
assert checking_string('Test') is True
assert checking_string('Інша мова') is True
assert checking_string(10) is False
assert checking_string('test') is False
assert checking_string('Test Test') is False
assert checking_string('TEST ') is False
assert checking_string('!Test') is False
assert checking_string(["Test", 15]) is False
assert checking_string(('Test', 10)) is False
assert checking_string({'Test', 10}) is False
assert checking_string({'Test': 10, 10: "Test"}) is False

# checking_string(input("Please, enter some text: "))
