#School management system

class School:
    def __init__(self, name,id):
        self.name = name
        self.id = id
        self.students = []
        self.teachers = []
        self.staff = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_staff(self, staff):
        self.staff.append(staff)
        
    def get_students(self):
        print("Students in",self.name)
        for student in self.students:
            print("Name:",student.name,"ID:",student.id,"Marks:",student.marks)

    def get_teachers(self):
        print("Teachers in",self.name)
        for teacher in self.teachers:
            print("Name:",teacher.name,"ID:",teacher.id,"Salary:",teacher.salary)

    def get_staff(self):
        print("Staff in",self.name)
        for staff in self.staff:
            print("Name:",staff.name,"ID:",staff.id,"Department:",staff.dept)
    
class Student:
    def __init__(self, name, id,marks):
        self.name = name
        self.id = id
        self.marks = marks
        
class Teacher:
    def __init__(self, name, id,salary):
        self.name = name
        self.id = id
        self.salary = salary

class Staff:
    def __init__(self, name, id,dept):
        self.name = name
        self.id = id
        self.dept=dept
        
SC=School("ABC School",1)
n=int(input("Enter the number of students: "))
for i in range(n):
    name=input("Enter the name of student: ")
    id=int(input("Enter the id of student: "))
    marks=int(input("Enter the marks of student: "))
    s=Student(name,id,marks)
    SC.add_student(s)
   
    
n=int(input("Enter the number of teachers: "))
for i in range(n):
    name=input("Enter the name of teacher: ")
    id=int(input("Enter the id of teacher: "))
    salary=int(input("Enter the salary of teacher: "))
    t=Teacher(name,id,salary)
    SC.add_teacher(t)
    
    

n=int(input("Enter the number of staff members: "))
for i in range(n):
    name=input("Enter the name of staff member: ")
    id=int(input("Enter the id of staff member: "))
    dept=input("Enter the department of staff member: ")
    st=Staff(name,id,dept)
    SC.add_staff(st)
    
for i in range(n):
    SC.get_students()
    SC.get_teachers()
    SC.get_staff()