#single level inheritance

class A:
    def method1(self):
        print("This is method 1 from class A")
class B(A):
    def method2(self):
        print("This is method 2 from class B")

b1=B()
b1.method1()
b1.method2()