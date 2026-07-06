print("=" * 45)
print("       RESTAURANT BILL SPLITTER")
print("=" * 45)

total_bill = float(input("Enter Total Bill Amount (₹): "))
people = int(input("Enter Number of People: "))

amount_per_person = total_bill / people

print("\n")
print("=" * 45)
print("             BILL DETAILS")
print("=" * 45)

print("Total Bill        : ₹", total_bill)
print("Number of People  :", people)
print("Each Person Pays  : ₹", round(amount_per_person, 2))

print("=" * 45)
print("Enjoy Your Meal! 🍕")
