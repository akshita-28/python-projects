print("="*40)
print("Student Grade Calculator")
print("="*40)
name=input("Enter your Name:")
physics=int(input("Enter your  PHYSICS Marks:"))
chemistry=int(input("Enter your CHEMISTRY Marks:"))
maths=int(input("Enter your MATHS Marks:"))
total = physics+chemistry+maths
percentage = total/3
print("/n")
print("="*40)
print("RESULT")
print("="*40)
print("STUDENT NAME:", name)
print("Percentage:",round(percentage,2))
if percentage >=90:
    print("Grade :A+")
elif percentage >=80:
    print("Grade :A")
elif percentage >=70:
    print("Grade:B")
elif percentage  >=60:
    print("Grade:C")
elif percentage >=50:
    print("Grade:D")
else:
    print("Grade: Fail")        