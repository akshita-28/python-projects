print("="*45)
print(" ELECTRICITY BILL CALCULATOR")
print("="*45)
Customer_name=input("Enter Customer Name :")
units=int(input("Enter Units Consumed:"))
if units <=100:
    bill =units * 5
elif units<= 200:
    bill =units *7
elif units <=300:
    bill = units*9
else:
    bill = units*12
print("\n")
print("="*45) 
print("BILL")
print("="*45)
print("Customer Name:",Customer_name)            
print("Units Consumed:",units)   
print("Total Bill:Rs",bill)
print("="*45)
print("Thank you")
