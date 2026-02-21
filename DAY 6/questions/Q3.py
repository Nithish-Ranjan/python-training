# Build a payment system for e commerce website. The system should allow users to make payments using different payment methods such as credit card, UPI
# cvv and pin should be hidden

class pay:
    def __init__(self,name,amt):
        self.name=name
        self.amt=amt
        self.__cvv=""
        self.__pin=""
    
    def set_cvv(self,cvv):
        self.__cvv=cvv
    def set_pin(self,pin):
        self.__pin=pin
        
    def show(self):
        print("Name:",self.name,"Amount:",self.amt)
        
    def get_cvv(self):
        return self.__cvv
    def get_pin(self):
        return self.__pin

n=int(input("Enter the number of payments: "))       
for i in range(n):
    p = pay(input("Enter name: "), float(input("Enter amount: ")))
    p.set_cvv(input("Enter CVV: "))
    p.set_pin(input("Enter PIN: "))
    p.show()
    print("CVV:",p.get_cvv())
    print("PIN:",p.get_pin())
    