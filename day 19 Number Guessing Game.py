print("=" * 45)
print("       NUMBER GUESSING GAME")
print("=" * 45)

secret_number = 7

guess = int(input("Guess the Number (1-10): "))

while guess != secret_number:

    if guess < secret_number:
        print("Too Low! Try Again.")

    else:
        print("Too High! Try Again.")

    guess = int(input("Guess Again: "))

print("\nCongratulations! 🎉")
print("You Guessed the Correct Number.")