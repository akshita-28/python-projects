print("="*45)
print(" FACTORIAL CALCULATOR")
print("="*45)
number=int(input("Enter a Number:"))
factorial=1
for i in range(1,number+1):
    factorial=factorial*i
print("Factorial of",number,"=",factorial)    

