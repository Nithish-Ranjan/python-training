# Multilevel inheritance

class Grand:
    def __init__(self,name,Pname,Cname):
        self.name=name
        self.Pname=Pname
        self.Cname=Cname
    def disp1(self):
        print("Hello, I am the grandparent and my name is",self.name)
        
class Parent(Grand):
    def __init__(self,name,Pname,Cname):
        super().__init__(name,Pname,Cname)
    def disp2(self):
        print("Hello, I am the parent and my name is",self.Pname)
        
class Child(Parent):
    def __init__(self,name,Pname,Cname):
        super().__init__(name,Pname,Cname)
    def disp3(self):
        print("Hello, I am the child and my name is",self.Cname)
        
c1=Child("swamy","Shiv","Nrj")
c1.disp1()
c1.disp2()
c1.disp3()