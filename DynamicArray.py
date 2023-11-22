# 1. Prompt the user for a number and create a list
num_items = int(input("Enter the number of items for the list: "))
my_list = []
for _ in range(num_items):
    item = int(input("Enter an integer: "))
    my_list.append(item)
print("List:", my_list)

# 2. Insert the score of 99 at position 1 within the list
my_list.insert(1, 99)
print("Updated List:", my_list)

# 3. Replace the value of 99 with the value 100
if 99 in my_list:
    idx = my_list.index(99)
    my_list[idx] = 100
print("Updated List:", my_list)

# 4. Create a second list and extend the first list with it
second_list = [500, 600, 700, 800, 900]
print("Second List:", second_list)
my_list.extend(second_list)
print("Extended List:", my_list)

# 5. Remove the value 800 from the first list
if 800 in my_list:
    my_list.remove(800)
print("List after removing 800:", my_list)

# 6. Remove the third item from the first list
if len(my_list) > 2:
    del my_list[2]
print("List after removing the third item:", my_list)

# 7. Create a list of grades
grades = ["A", "B", "C", "A", "A", "C"]

# 8. Display a count of the number of A grades
count_A = grades.count("A")
print("Count of A grades:", count_A)

# 9. Display the index of the first B grade
if "B" in grades:
    idx_B = grades.index("B")
    print("Index of the first B grade:", idx_B)

# 10. Look for grade of F in the grades list
if "F" not in grades:
    print("F is not in the list.")

# 11. Clear the second list of integers
second_list.clear()
print("Cleared Second List:", second_list)

# 12. Delete the second list (will raise an error because the list no longer exists)
# del second_list
# print(second_list)

# 13. Create a list of players
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

# 14. Sort the list of players
players.sort()
print("Sorted List of Players:", players)

# 15. Make a copy of the list of players called players2
players2 = players.copy()
print("Copy of Players List (players2):", players2)

# 16. Reverse the order of players2
players2.reverse()
print("Reversed Players2:", players2)
print("Original Players List:", players)
