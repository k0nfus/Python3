# Lists
tasks = ["install python", "learn python", "take a break"]
zahlen = [1, 2, 3]

print(tasks)
print(zahlen[-1])

# Nested Lists
wild = [tasks, zahlen]

print(wild)
print(wild[0][1])
print(wild[1][2])

# List Range
list_range = list(range(1,5))

print(list_range)

# Changing Data
list_range[0] = "42"

print(list_range)

# Adding Data
list_range.append(5)

print(list_range)

# Deleting Data
list_range[1:4] = []

print(list_range)

# Replace Data

list_range[0] = 23

print(list_range)