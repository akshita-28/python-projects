print("=" * 45)
print("        PALINDROME CHECKER")
print("=" * 45)

number = int(input("Enter a Number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print()

if original == reverse:
    print(original, "is a Palindrome Number ✅")
else:
    print(original, "is NOT a Palindrome Number ❌")