#single level inheritance

class A:  #parent class or base class
    def method1(self):
        print("This is method 1 from class A")
class B(A):  #child class or derived class
    def method2(self):
        print("This is method 2 from class B")

b1=B()
b1.method1()
b1.method2()