# method overloading
# method overloading is not supported in python but we can achieve it by using default arguments or variable length arguments

class animal:
    def eat(self):
        print("Eating")
        
    def eat(self,food):
        print("Eating",food)
        
class Dog(animal):
    def eat(self,food):
        print("Eating",food,"like a dog")
        
d=Dog()
d.eat("bone") # Eating bone like a dog
# d.eat() # TypeError: eat() missing 1 required positional argument: 'food'
a=animal()
# a.eat() # TypeError: eat() missing 1 required positional argument: 'food'
a.eat("food") # Eating food