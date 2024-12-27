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

class bike(vehicle):
    pass
def makeCar():
    
    start = input("build a new car? y/n ")

    if "y" in start:
        car_brand = input("what brand is the car? ")
        car_model = input("what model is the car? ")
        c = car (car_brand,car_model)
        print(c)
        makeCar()
    else:
        print("come back when you want a car...ok bub?")
        makeBike()
        exit()
        

def makeBike():

    start = input("would you like to make a bike?")

    if "y" in start:
        bike_brand = input("what brand?: ")
        bike_model = input("what model:  ")
        b = bike (bike_brand,bike_model)
        print(b)
        makeBike()
    else:
        print("aye get outta here if you ain't talking bike")
        return makeCar()
        exit()


begin = input("start? y/n")
if "y" in begin:
    makeCar()
else:
    print("scram")
    exit()