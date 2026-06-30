print("="*45)
print(" SMALLEST OF THREE NUMBERS")
print("="*45)
num1=float(input("Enter First Number:"))
num2=float(input("Enter Second Number:"))
num3=float(input("Enter Third Number:"))
print("\n")
if num1<=num2 and num1<=num3:
    print("Smallest Number is:",num1)
elif num2<=num1 and num2<=num3:
    print("Smallest Number is:",num2)
else:
    print("Smallest Number is :",num3)        