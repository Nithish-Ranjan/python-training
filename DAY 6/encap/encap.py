# # Encapsulation is the process of hiding the internal details of an object and only exposing a public interface. This allows us to protect the internal state of an object and prevent it from being modified directly.

# # __private_variable is a convention in Python to indicate that a variable is intended to be private and should not be accessed directly from outside the class.
# # _protected_variable is a convention in Python to indicate that a variable is intended to be protected and should not be accessed directly from outside the class, but can be accessed by subclasses.

# class exp:
#     a="PUBLIC"
#     _b="PROTECTED"
#     __c="PRIVATE"
    
#     def get_private(self):
#         return self.__c
    
# class child(exp):
#     def get_protected(self):
#         return self._b
    
# obj=exp()
# print(obj.a) # PUBLIC
# print(obj.get_private()) 
# child_obj=child()
# print(child_obj.get_protected()) 

class factory:
    def __init__(self,location):
        self.__location=location
        
    def set_location(self,loc):
        self.__location=loc
        
    def get_location(self):
        return self.__location
    
f1=factory("India")
f1.set_location("USA")
print(f1.get_location()) # USA