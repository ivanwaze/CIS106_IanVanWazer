def compute_exam_avg(exam1,exam2,exam3):
  sum = exam1 + exam2 + exam3
  total = 300
  percentage = (sum/total) * 100
  average = sum/3
  points = exam1 + exam2 + exam3
  return average,points

#define variables
lastname= str(input("Enter last name"))
exam1 = float(input("Enter your exam 1 grade"))
exam2 = float(input("Enter your exam 2 grade"))
exam3 = float(input("Enter your exam 3 grade"))

average, points = compute_exam_avg(exam1,exam2,exam3)
print("Student name:",lastname)
print("Your average is ", average)
print("Your points are ", points)