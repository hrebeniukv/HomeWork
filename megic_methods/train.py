from megic_methods.wagon import Wagon


class Train:
    def __init__(self, *wagons):
        self.__wagons = sorted([wagon for wagon in wagons])

    def __len__(self):
        return len(self.__wagons)

    def __str__(self):
        train = "<=[HEAD]"
        for i in self.__wagons:
            train += f"-[{i.get_number()}]"
        return train

    def new_wagon(self, wagon: Wagon):
        self.__wagons.append(wagon)



