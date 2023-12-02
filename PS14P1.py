import datetime

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@email.com"
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        return day.weekday() < 5

    def calculate_bonus(self, bonus_rate):
        return self.pay * bonus_rate

# Existing code from video

# Example usage:
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

# Calculate and print bonus for an employee
bonus_rate = 0.1  # Example bonus rate (10%)
bonus_emp_1 = emp_1.calculate_bonus(bonus_rate)
print(f"Bonus for {emp_1.fullname()}: ${bonus_emp_1:.2f}")
