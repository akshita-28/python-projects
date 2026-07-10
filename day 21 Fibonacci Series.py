print("=" * 45)
print("         FIBONACCI SERIES")
print("=" * 45)

terms = int(input("Enter Number of Terms: "))

first = 0
second = 1

print("\nFibonacci Series:")

for i in range(terms):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number