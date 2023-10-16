# Define cost per credit for in-district and out-of-district students
cost_per_credit = {
    "I": 250.00,
    "O": 500.00
}

# Read data from the text file
with open('P5d.txt') as file:
    lines = file.readlines()

# Process the data
student_data = []
for line in lines:
    last_name, district_code, credits_taken = line.strip().split(',')
    credits_taken = int(credits_taken)
    student_data.append((last_name, district_code, credits_taken))

# Initialize variables for total tuition and number of students
total_tuition = 0
num_students = len(student_data)

# Calculate tuition and display information
for last_name, district_code, credits_taken in student_data:
    tuition_owed = credits_taken * cost_per_credit[district_code]
    total_tuition += tuition_owed
    print(f"Last Name: {last_name}, Credits Taken: {credits_taken}, Tuition Owed: {tuition_owed:.2f}")

# Display total tuition and number of students
print(f"Total Tuition Owed: {total_tuition:.2f}")
print(f"Number of Students: {num_students}")

