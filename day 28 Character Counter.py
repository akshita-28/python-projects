print("=" * 45)
print("        CHARACTER COUNTER")
print("=" * 45)

text = input("Enter a Sentence: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0

for ch in text:

    if ch.isupper():
        uppercase += 1

    elif ch.islower():
        lowercase += 1

    elif ch.isdigit():
        digits += 1

    elif ch == " ":
        spaces += 1

print()
print("=" * 45)
print("              RESULT")
print("=" * 45)

print("Uppercase Letters :", uppercase)
print("Lowercase Letters :", lowercase)
print("Digits            :", digits)
print("Spaces            :", spaces)
print("Total Characters  :", len(text))