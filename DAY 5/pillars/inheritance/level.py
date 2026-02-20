# multilevel inheritance 

class A:
    def method1(self):
        print("this is method 1 from class A")

class B(A):
    def method2(self):
        print("this is method 2 from class B")
        
class C(A):
    def method3(self):
        print("this is method 3 from class C")
        
c1=C()
c1.method1()
c1.method3()

b1=B()
b1.method1()
b1.method2()
