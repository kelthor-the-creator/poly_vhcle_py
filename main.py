# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return '{} {} ' .format(self.brand,self.model)

class car(vehicle):
    pass
def makeCar():


    start = input("build a new car? y/n")

    if "y" in start:
        car_brand = input("what brand is the car?")
        car_model = input("what model is the car?")
        c = car(car_brand,car_model)
        print(c)

        return 
    else:
        print("come back when you want a car...ok bub?")
        exit()
        


makeCar()