# Arrays containing names and scores
l_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
ex_scores = [85, 90, 78, 92, 88, 75, 84, 79, 93, 87]

# Function to display names and scores
def display_names_and_scores(names, scores):
    for i in range(len(names)):
        print(f"{names[i]} - Exam Score: {scores[i]}")

# Function to display names and exam scores in reverse order
def display_reverse_names_and_scores(names, scores):
    for i in range(len(names) - 1, -1, -1):
        print(f"{names[i]} - Exam Score: {scores[i]}")

# Displaying names and exam scores
print("Names and Exam Scores:")
display_names_and_scores(l_names, ex_scores)

print("\nNames and Exam Scores in Reverse Order:")
display_reverse_names_and_scores(l_names, ex_scores)