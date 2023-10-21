def get_pay_rate(job_code):
    if job_code == 'L':
        return 25
    elif job_code == 'A':
        return 30
    elif job_code == 'J':
        return 50
    else:
        return 0

def calculate_gross_pay(rate, hours_worked):
    if hours_worked <= 40:
        return rate * hours_worked
    else:
        overtime_hours = hours_worked - 40
        return (rate * 40) + (1.5 * rate * overtime_hours)

total_gross_pay = 0

try:
    while True:
        last_name = input("Enter last name (Ctrl+Z to stop): ")
        job_code = input("Enter job code (L/A/J): ")
        hours_worked = float(input("Enter hours worked: "))

        rate = get_pay_rate(job_code)
        if rate == 0:
            print(f"Invalid job code '{job_code}'. Please enter L, A, or J.")
            continue

        gross_pay = calculate_gross_pay(rate, hours_worked)
        total_gross_pay += gross_pay

        print(f"Last Name: {last_name}, Gross Pay: ${gross_pay:.2f}\n")

except EOFError:
    pass

print(f"Total Gross Pay: ${total_gross_pay:.2f}")
