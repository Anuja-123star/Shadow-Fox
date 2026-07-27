justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Original List:", justice_league)

# Task 1
print("\n1. Number of members:", len(justice_league))

# Task 2
justice_league.extend(["Batgirl", "Nightwing"])
print("\n2. After adding Batgirl and Nightwing:")
print(justice_league)

# Task 3
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3. Wonder Woman becomes the leader:")
print(justice_league)

# Task 4
justice_league.remove("Green Lantern")
a = justice_league.index("Aquaman")
justice_league.insert(a + 1, "Green Lantern")
print("\n4. Green Lantern moved between Aquaman and Flash:")
print(justice_league)

# Task 5
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n5. New Justice League:")
print(justice_league)

# Task 6
justice_league.sort()
print("\n6. Alphabetically sorted list:")
print(justice_league)

print("\nNew Leader:", justice_league[0])
