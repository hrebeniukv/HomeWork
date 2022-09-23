# Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".


def cheking_symbol(entered_data):

    try:
        word, symbol_index = entered_data.split(" ")
        symbol_index = int(symbol_index)
        sear_leter = word[symbol_index]

    except IndexError:
        return "The word is too short!"

    except ValueError:
        return "Entered data are wrong, or you didn't enter any data!"

    except Exception:
        return "Something was wrong"

    else:
        return f"The {symbol_index} symbol in {word} is \'{sear_leter}\'."


input_data = input("Enter by spacing the word and symbol which need to find in the entered word: ")

print(cheking_symbol(input_data))



# Написати цикл, який буде вимагати від користувача ввести слово,
# в якому є буква "о" (враховуються як великі так і маленькі). Цикл не повинен завершитися,
# якщо користувач ввів слово без букви о.


while True:

    input_data = input("Please, enter the word which contains \'o\'. ").lower()

    if "o" in input_data:
        print(f"The letter \'o\' is under the index {input_data.find('o')}")
        break

    elif not input_data:
        print("You didn\'t enter any data")

    elif input_data.isdigit():
        print("Entered data contains only numbers!")

    else:
        print("The word doesn't contain the leter \'o\'.")
