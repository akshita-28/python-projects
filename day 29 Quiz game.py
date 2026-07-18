print("=" * 45)
print("          PYTHON QUIZ APP")
print("=" * 45)

score = 0

print("\nQ1. Who developed Python?")
print("a. James Gosling")
print("b. Guido van Rossum")
print("c. Dennis Ritchie")
print("d. Bjarne Stroustrup")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "b":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌")

print("\nQ2. Which keyword is used for loops?")
print("a. repeat")
print("b. loop")
print("c. for")
print("d. iterate")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "c":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌")

print("\nQ3. Which function is used to take input?")
print("a. print()")
print("b. scan()")
print("c. input()")
print("d. read()")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "c":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌")

print("\n" + "=" * 45)
print("Final Score:", score, "/3")
print("=" * 45)