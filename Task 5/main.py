import random

# Task 1
count6 = 0
count1 = 0
twosix = 0
prev = 0

for i in range(20):
    x = random.randint(1, 6)
    print(x)

    if x == 6:
        count6 += 1
    if x == 1:
        count1 += 1
    if prev == 6 and x == 6:
        twosix += 1

    prev = x

print("6 appeared:", count6)
print("1 appeared:", count1)
print("Two 6s in a row:", twosix)

# Task 2
total = 0

for i in range(10):
    total += 10
    print("Completed", total, "jumping jacks")
    print(100 - total, "jumping jacks remaining")

print("Congratulations! You completed the workout.")
