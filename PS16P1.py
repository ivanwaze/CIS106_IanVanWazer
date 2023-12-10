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

  def calculate_bonus(self, bonus_rate):
      return self.pay * bonus_rate


class Manager(Employee):
  def long_term_bonus(self):
      return self.pay * 0.4  # 40% of the salary for long-term bonus


# Test the Manager class
manager = Manager('Alice', 'Johnson', 80000)  # Creating a manager with a salary of $80,000
print(f"{manager.fullname()} - Salary: ${manager.pay}")

bonus = manager.long_term_bonus()
print(f"Long-term Bonus for {manager.fullname()}: ${bonus:.2f}")
