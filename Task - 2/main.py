def format_values(num, char):
    return "First Argument: {} , Second Argument: {}".format(num, char)

result = format_values(145, 'o')
print(result)
print(repr(result))

pi = 3.14
radius = 84

area = pi * radius * radius
water = area * 1.4

print("Area of the pond:", area)
print("Total water in the pond:", int(water), "liters")

distance = 490
time = 7 * 60

speed = distance / time

print("Speed:", int(speed), "meters/second")
