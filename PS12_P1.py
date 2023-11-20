# Assignment
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

# Function to display names
def display_names(names):
    for name in names:
        print(name)

# Function to display names in reverse order
def display_reverse(names):
    for i in range(len(names) - 1, -1, -1):
        print(names[i])

# Displaying names
print("Names:")
display_names(last_names)

print("\nNames in Reverse Order:")
display_reverse(last_names)
