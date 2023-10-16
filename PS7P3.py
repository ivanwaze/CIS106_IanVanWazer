# Define bonus rates
bonus_rates = {
    "100000.00 and up": 0.20,
    "50000.00": 0.15,
    "All other salaries": 0.10
}

# Read data from the text file
with open('P3d.txt') as file:
    lines = file.readlines()

# Process the data
employee_data = []
for line in lines:
    line = line.strip()
    if line.replace('.', '', 1).isdigit():
        salary = float(line)
        employee_data[-1].append(salary)
    else:
        last_name = line
        employee_data.append([last_name])

# Calculate bonuses and display information
total_bonus = 0
for entry in employee_data:
    last_name, salary = entry[0], entry[1]
    for salary_range, bonus_rate in bonus_rates.items():
        if salary_range == "100000.00 and up" and salary >= 100000.00:
            bonus = salary * bonus_rate
        elif salary_range == "50000.00" and salary == 50000.00:
            bonus = salary * bonus_rate
        elif salary_range == "All other salaries" and salary < 100000.00 and salary != 50000.00:
            bonus = salary * bonus_rate

    total_bonus += bonus
    print(f"Last Name: {last_name}, Salary: {salary}, Bonus: {bonus:.2f}")

# Display total bonuses
print(f"Total Bonuses Paid Out: {total_bonus:.2f}")

