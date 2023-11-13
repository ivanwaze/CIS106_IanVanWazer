def bowl_avg (score1,score2,score3):
  sum= score1 + score2 + score3
  average = (sum / 3)
  return average



lastname = str(input("Enter your last name: "))
score1 = float(input("Enter your first game score"))
score2 = float(input("Enter your second game score"))
score3 = float(input("Enter your third game score"))
handicap = str(input("What is your handicap"))
average = bowl_avg(score1,score2,score3)
subtract = 210- average
handicap = subtract + 0.90
print("Your handicap is: ",handicap)
print("Your last name is: ",lastname)
print("Your average is: ",average)