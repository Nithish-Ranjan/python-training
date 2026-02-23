# Decorators 

# It is a function that modifies another function without changing its actual code

# class A:
#     @property
#     def show(self):
#         print("hello !")
        
# o = A()
# o.show

def mydeco(param):
    def wrapper():
        print("hello!")
        param()
        print("wonderful!")
    return wrapper

@mydeco
def hello():
    print("python!")
    
hello()