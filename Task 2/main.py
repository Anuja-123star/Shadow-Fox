# Task 1
def show(num, ch):
    return "Binary representation of {} is {:o}".format(num, num)

print("Task 1")
print(show(145, 'o'))
print("Representation used: Octal")

# Task 2
print("\nTask 2")
pi = 3.14
r = 84

area = pi * r * r
water = int(area * 1.4)

print("Area of pond:", area)
print("Total water:", water, "liters")

# Task 3
print("\nTask 3")
distance = 490
time = 7 * 60

speed = int(distance / time)

print("Speed:", speed, "m/s")
