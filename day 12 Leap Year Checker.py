print("=" *45)
print(" LEAP YEAR  CHECKER ")
print("="*45)
year = int(input("Enter a year:"))
print()
if (year % 400 == 0 ) or (year % 4 == 0 and year %100 !=0):
    print(year,"is a leap year")
else:
    print(year,"is NOT a leap year:")
        