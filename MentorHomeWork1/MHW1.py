import requests
from pprint import pprint
from tabulate import tabulate


# завдання 1
# урл http://api.open-notify.org/astros.json
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті (дані не фейкові, оновлюються в режимі реального часу)

# first output in table

def peple_on_orbit(url: str):
    response = requests.get(url)
    response_json = response.json()
    print(tabulate(response_json["people"], headers='keys', tablefmt="grid", stralign='center'))


url = "http://api.open-notify.org/astros.json"
peple_on_orbit(url)


# seconf output

def peple_on_orbit(url: str):
    response = requests.get(url)
    response_json = response.json()

    for person in response_json["people"]:
        pprint(person)


url = "http://api.open-notify.org/astros.json"
peple_on_orbit(url)


# завдання 2
# апі погоди (всі токени я для вас вже прописав)
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
# де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv)
# погода змінюється, як і місто. яке ви введете
# роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране

# url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric".format(
#     city_name="odesa")
#
# response = requests.get(url)
# response_json = response.json()
# pprint(response_json)


def weather(url: str, city: str):
    response = requests.get(url.format(city_name=city))
    response_json = response.json()
    print(
        f"The wind speed in {city} is {response_json['wind']['speed']} m/s and "
        f"air temperature is {response_json['main']['temp']} degrees Celsius")


city = input("Please enter the city name, only in English: ").capitalize()
url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric"
weather(url, city)
