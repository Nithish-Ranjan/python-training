'''generate bill for the given quantity and price of the item'''
cust_id=1           #customer id
price=2000          #price of the item
quantity=5          #quantity of the item
coupon_code= True   #coupon code is applied or not
method = input("enter payment method: ")        #payment method
method = method.upper()  #convert payment method to uppercase for consistency
total = price * quantity    #total bill amount
discount = 0

#if coupon is true and total is greater than 5000 then apply 500 discount

if coupon_code and total > 5000:
    discount = 500

final_amount = total - discount

if method == "UPI":
    final_amount = final_amount * 0.95  #5% discount for UPI payment
elif method == "CARD":
    final_amount = final_amount * 0.98  #2% discount for card payment
else:
    print("No additional discount for cash payment.")
    
final_amount = final_amount + final_amount * 0.18  #add 18% GST to the final amount

print("Customer ID:", cust_id)
print("Price per item:", price) 
print("Quantity:", quantity)
print("Total bill amount before discount:", total)
print("Discount applied:", discount)
print("Final bill amount:", final_amount)