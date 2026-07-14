import time

print("=" * 45)
print("         COUNTDOWN TIMER")
print("=" * 45)

seconds = int(input("Enter Time in Seconds: "))

while seconds > 0:
    print("Time Left:", seconds, "seconds")
    time.sleep(1)
    seconds -= 1

print("\n⏰ Time's Up!")