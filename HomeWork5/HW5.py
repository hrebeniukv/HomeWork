# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд. "а, е, и, і, о, у, я, ю, є, ї"


def words_checking(cheking_string: list, letters: list) -> int:
    letter_counter = 0
    for world in cheking_string:

        neighbor_counter = 0
        for i in range(len(world)):
            if world[i] in letters:
                neighbor_counter += 1
            else:
                neighbor_counter = 0

            if neighbor_counter == 2:
                letter_counter += 1
                break
    return letter_counter


letters = ["а", "е", "и", "і", "о", "у", "я", "ю", "є", "ї", "й"]
test_phrase = input("Please enter the test phrase. Only in Ukrainian!!!: ").lower().split(" ")
print(words_checking(test_phrase, letters))


# Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами:
# { "cito": 47.999,
#   "BB_studio" 42.999,
#   "momo": 49.999,
#   "main-service": 37.245,
#   "buy.now": 38.324,
#   "x-store": 37.166,
#   "the_partner": 38.988,
#   "sota": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів,
# ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:
#
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"

def store_filter_by_price(store_list: dict, lower_limit: float, upper_limit: float) -> list:
    filtred_list = []
    for store, price in store_list.items():
        if lower_limit <= price <= upper_limit:
            filtred_list.append(store)

    return filtred_list


store_list = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "sota": 37.720,
    "rozetka": 38.003,
    "EuroAGD": 35.9,
    "MediaExpres": 37.339
}

lower_limit = 35.9
upper_limit = 37.339

filter_res = store_filter_by_price(store_list, lower_limit, upper_limit)
print(f"list of stores which mach to your filters: {', '.join(filter_res)}")
