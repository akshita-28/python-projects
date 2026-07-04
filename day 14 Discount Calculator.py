print("=" * 45)
print("        DISCOUNT CALCULATOR")
print("=" * 45)

customer_name = input("Enter Customer Name: ")
amount = float(input("Enter Shopping Amount: ₹"))

if amount >= 10000:
    discount = amount * 0.20

elif amount >= 5000:
    discount = amount * 0.10

elif amount >= 2000:
    discount = amount * 0.05

else:
    discount = 0

final_amount = amount - discount

print("\n")
print("=" * 45)
print("              BILL")
print("=" * 45)

print("Customer Name :", customer_name)
print("Shopping Amount : ₹", amount)
print("Discount : ₹", round(discount, 2))
print("Final Amount : ₹", round(final_amount, 2))

print("=" * 45)
print("Thank You For Shopping 😊")