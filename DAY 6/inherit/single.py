class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print (f"Hello, my name is {self.name} and I am an animal.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def show(self):
        print (f"Woof! My name is {self.name} and I am a {self.breed}.")
        
d1=Dog("LORD", "Golden Retriever")
d1.speak()
d1.show()