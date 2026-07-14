print("=" * 45)
print("      ARMSTRONG NUMBER CHECKER")
print("=" * 45)

number = int(input("Enter a Number: "))

original = number
sum = 0

while number > 0:
    digit = number % 10
    sum = sum + (digit ** 3)
    number = number // 10

print()

if sum == original:
    print(original, "is an Armstrong Number ✅")
else:
    print(original, "is NOT an Armstrong Number ❌")

    