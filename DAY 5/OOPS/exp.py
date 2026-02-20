class bag:
    def __init__(self,zips,color,price):
        self.zips=zips
        self.color=color
        self.price=price
    
    def show(self):
        print("this bag has zips",self.zips,"and color is",self.color,"and price is",self.price)
        
for i in range(3):
    zips=int(input("Enter number of zips: "))
    color=input("Enter color of bag: ")
    price=int(input("Enter price of bag: "))
    b1=bag(zips,color,price)
    b1.show()