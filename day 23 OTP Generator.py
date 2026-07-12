import random

print("=" * 45)
print("          OTP GENERATOR")
print("=" * 45)

otp = ""

for i in range(6):
    digit = random.randint(0, 9)
    otp = otp + str(digit)

print("\nYour OTP is:", otp)