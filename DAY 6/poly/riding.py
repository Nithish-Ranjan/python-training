# overriding the method of the parent class

class Vehicle:
    def ride(self):
        print("Riding a vehicle")
        
class Bike(Vehicle):
    def ride(self):
        print("Riding a bike")
        
cls=Bike()
cls.ride() # Riding a bike