# 1. Describe any object of your choice in the class. I want the object to be printed to the console in the following format:
# class_name: {
#     key: value
# }


class School:
    def __init__(self, name: str, qty_teachers: int, qty_personal: int, qty_students: int, address: str):
        self.name = name
        self.qty_teachers = qty_teachers
        self.qty_personal = qty_personal
        self.qty_students = qty_students
        self.address = address

    def __str__(self):
        obj_attribute = list(self.__dict__.items())
        attributes = ""
        for i in range(len(obj_attribute)):
            if i < len(obj_attribute) - 1:
                attributes += f"\n\t{obj_attribute[i][0]}: {obj_attribute[i][1]}"
            if i == len(obj_attribute) - 1:
                attributes += f"\n\t{obj_attribute[i][0]}: {obj_attribute[i][1]}\n"

        return f"{self.__class__.__name__}: {{{attributes}}}"


school = School('New', 15, 12, 34, 'Kyivska 34/5, 32-031, Chernichiv')
print(school)



# 2.Describe the Train object. The class must contain fields and a method for adding wagons
# (it is necessary to add objects, instances of the wagon class).
# Describe the class TrainCar/Wagon together with the train.
# The car must contain a list of passengers and allow adding passengers. In the TrainCar can be 10 passengers for example.
# When using the len function on a TrainCar, I want to see the number of passengers. When using len on a train,
# I want to see a list of W0agons/trainCars without a locomotive. Each wagon must have a number.
# When printing a wagon to the console, I want to see the following "[n]" where n is the number of the wagon.
from megic_methods.train import Train
from megic_methods.wagon import Wagon

wagon1 = Wagon(["tomas", "jeremy", "edward"], 3)
wagon2 = Wagon(["tom", "henri", "elvis"], 2)
wagon3 = Wagon(["anet", "irvin", "gorge"], 1)

train = Train(wagon2, wagon3,wagon1)



