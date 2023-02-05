class Wagon:

    def __init__(self, passengers_list: list, number: int):
        self.__passengers: list = passengers_list
        self.__number: int = number

    def __str__(self):

        return f"[{self.__number}]"

    def __len__(self):
        return len(self.__passengers)

    def __eq__(self, other):
        return self.__number == other.__number

    def __lt__(self, other):
        return self.__number < other.__number

    def __gt__(self, other):
        return self.__number > other.__number

    def get_number(self):
        return self.__number

    def new_passenger(self, name: str):
        self.__passengers.append(name)



