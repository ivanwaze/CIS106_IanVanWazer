class Student:
  def __init__(self, first_name, last_name, district_code, enrolled_credits):
      self.first_name = first_name
      self.last_name = last_name
      self.district_code = district_code
      self.enrolled_credits = enrolled_credits

  def compute_tuition(self):
      if self.district_code == 'I':
          tuition_owed = self.enrolled_credits * 250.00
      else:
          tuition_owed = self.enrolled_credits * 500.00
      return tuition_owed

# Testing the class
student1 = Student("John", "Doe", "I", 12)  # In-district student with 12 credits
tuition1 = student1.compute_tuition()
print(f"{student1.first_name} {student1.last_name} owes ${tuition1:.2f} in tuition.")

student2 = Student("Ian", "McKellan", "O", 15)  # Out-of-district student with 15 credits
tuition2 = student2.compute_tuition()
print(f"{student2.first_name} {student2.last_name} owes ${tuition2:.2f} in tuition.")
