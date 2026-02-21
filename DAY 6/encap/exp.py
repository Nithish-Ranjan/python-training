class Student:
    def __init__(self):
        self.__marks=0
    
    def set_marks(self,value):
        if 0<=value<=100:
            self.__marks=value
        else:
            print("Invalid marks. Please enter marks between 0 and 100.")
            
    def get_marks(self):
        return self.__marks
    
ob1=Student()
ob1.set_marks(90)
print(ob1.get_marks()) # 90
