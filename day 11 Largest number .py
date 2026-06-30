print("="*40)
print(" LARGEST OF THREE NUMBERS")
print("="*40)
num1= float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))
print("\n")
if num1>=num2 and num1>=num3:
    print("Largest number is:",num1)
elif num2>=num1 and num2>=num3:
    print("Largest number is:",num2) 
else:
    print("Largest number is:",num3)       