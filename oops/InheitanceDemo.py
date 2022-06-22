class Vehicle():

    vname=""
    make_year=0

class Car(Vehicle):

    def getCarData(self):
        self.vname = input("enter car name")
        self.make_year = int(input("enter make year of car"))

    def printCarData(self):
        print("car name = ",self.vname)    
        print("car make uear =",self.make_year)


class Bike(Vehicle):

    def getBikeData(self):
        self.vname = input("Bike bike name")
        self.make_year = int(input("Bike make year of car"))

    def printBikData(self):
        print("Bike name = ",self.vname)    
        print("Bike make uear =",self.make_year)


c = Car()
c.getCarData()
c.printCarData()

b  = Bike()
b.getBikeData()
b.printBikData()