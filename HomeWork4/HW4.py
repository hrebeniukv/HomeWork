# 1. Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Зауважте, що lst1 не є статичним і може формуватися динамічно.


def str_list(enter_data: list) -> list:
    lst2 = [i for i in enter_data if type(i) is str]
    return lst2


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(str_list(lst1))


# 2.Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
# Напишіть код, який видалить з нього всі числа, які менше 21 і більше 74.

def renove_numbers(test_list: list) -> list:
    for number in test_list[::-1]:
        if number < 21 or number > 74:
            test_list.remove(number)

    return test_list


list1 = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44, 74, 21, 20, 75]
print(renove_numbers(list1))


# 3.Є стрінг з певним текстом (можна скористатися input або константою). Напишіть код,
# який визначить кількість слів в цьому тексті, які закінчуються на 'о'.


def count_letter(enter_data: str) -> int:
    counter_symbol = 0
    for i in enter_data.lower().split(" "):
        if i[-1] == "o":
            counter_symbol += 1
    return counter_symbol


test_string = input("Enter test string: ")
print(count_letter(test_string))
