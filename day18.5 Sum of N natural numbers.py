print("="*45)
print("SUM OF FIRST N NATURAL NUMBERS")
print("="*45)
number=int(input("Enter a Number:"))
sum=0
for i in range (1,number+1):
    sum=sum + i
print()
print("Sum of First",number,"Natural Numbers=",sum)    
