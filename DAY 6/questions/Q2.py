# Company wants to calculaaet salary of empployes
# Each employee has name id
# there are 3 types of employees  full time, part time and intern

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class FullTimeEmployee(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
    def show(self):
        print("Name:",self.name,"ID:",self.id,"Salary:",self.salary)
        
class PartTimeEmployee(Employee):
    def __init__(self, name, id, hourly_rate, hours_worked):
        super().__init__(name, id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def show(self):
        print("Name:",self.name,"ID:",self.id,"Hourly Rate:",self.hourly_rate,"Hours Worked:",self.hours_worked,"Salary:",self.hourly_rate * self.hours_worked)
        
class Intern(Employee):
    def __init__(self, name, id, stipend):
        super().__init__(name, id)
        self.stipend = stipend
    def show(self):
        print("Name:",self.name,"ID:",self.id,"Stipend:",self.stipend)
      
n=int(input("Enter the number of employees: "))
employees = []  
for i in range(n):
    emp_type = input("Enter the type of employee (full-time, part-time, intern): ")
    name = input("Enter the name of employee: ")
    id = int(input("Enter the id of employee: "))
    
    if emp_type == "full-time":
        salary = float(input("Enter the salary of full-time employee: "))
        emp = FullTimeEmployee(name, id, salary)
    elif emp_type == "part-time":
        hourly_rate = float(input("Enter the hourly rate of part-time employee: "))
        hours_worked = float(input("Enter the hours worked by part-time employee: "))
        emp = PartTimeEmployee(name, id, hourly_rate, hours_worked)
    elif emp_type == "intern":
        stipend = float(input("Enter the stipend of intern: "))
        emp = Intern(name, id, stipend)
    else:
        print("Invalid employee type. Skipping.")
        continue
    
    employees.append(emp)
    
for i in range(n):
    employees[i].show()