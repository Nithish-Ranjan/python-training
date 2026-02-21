# OOP'S 

# Class and Object

# Class: A class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.
# Object: An object is an instance of a class. It is a specific realization of the class, with its own unique set of attributes and behaviors.

# class STD:
#     name="NRJ"
#     course="Python"
#     def into(self,name,course):
#         print("Hello I am",self.name,"and I am learning",self.course)
        
# print(STD.name)
# print(STD.course)
# s1=STD()
# s1.into("topper","web dev")

# class STD:
#     def __init__(self,name,course):
#         self.name=name
#         self.course=course
#     def into(self):
#         print("Hello I am",self.name,"and I am learning",self.course)
# s1=STD("NRJ","Python")
# s1.into()

# STD("mallu","java").into()


# class STD:
#     def __init__(self,name,course,age=19):
#         self.name=name
#         self.course=course
#         self.age=age
#     def into(self):
#         print("Hello I am",self.name,"and I am learning",self.course,"my age is ",self.age)

# for i in range(3):
#     name=input("Enter your name: ")
#     course=input("Enter your course: ")
#     s1=STD(name,course)
#     s1.into()

class STD:
    school_name="BITM School"
    def __init__(self,name,course):
        self.name=name
        self.course=course
    def into(self):
        print("Hello I am",self.name,"and I am learning",self.course)
        
    @classmethod
    def show(cls):
        print("hello",cls.school_name)
        
    @staticmethod
    def add(a,b):
        print("Sum of",a,"and",b,"is",a+b)
s1=STD("NRJ","Python")
s1.into()
s1.show()
STD.add(5,3)

#types of method
# 1. Instance method: A method that operates on an instance of the class and has access to the instance's attributes and other methods. It is defined without any decorators and takes 'self' as the first parameter.
# 2. Class method: A method that operates on the class itself and is defined using the @classmethod decorator.
# 3. Static method: A method that does not operate on an instance or the class and is defined using the @staticmethod decorator. It does not take 'self' or 'cls' as a parameter.



