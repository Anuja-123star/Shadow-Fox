# Task 1
print("Task 1 - BMI Calculator")

height = 1.75
weight = 70

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")

# Task 2
print("\nTask 2 - Find Country")

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = "Chennai"

if city in australia:
    print(city, "is in Australia")
elif city in uae:
    print(city, "is in UAE")
elif city in india:
    print(city, "is in India")
else:
    print("City not found")

# Task 3
print("\nTask 3 - Check Two Cities")

city1 = "Mumbai"
city2 = "Delhi"

country1 = ""
country2 = ""

if city1 in australia:
    country1 = "Australia"
elif city1 in uae:
    country1 = "UAE"
elif city1 in india:
    country1 = "India"

if city2 in australia:
    country2 = "Australia"
elif city2 in uae:
    country2 = "UAE"
elif city2 in india:
    country2 = "India"

if country1 == country2 and country1 != "":
    print("Both cities are in", country1)
else:
    print("They don't belong to the same country")
