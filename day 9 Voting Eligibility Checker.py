print("=" *40)
print("   VOTTING ELIGIBILITY CHECKER:")
print("=" *40)
name =input("Enter Your Name:")
age = int(input("Enter your Age:"))
print("\n")
if age >=18:
    print("Hello,",name)
    print("You are Eligible to Vote.")
else:
    print("Hello,",name )
    print("You are not Eligible to Vote.")    