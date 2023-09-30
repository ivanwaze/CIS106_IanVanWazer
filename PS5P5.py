print(" Enter last name ")
name = input()
print(" Input salary ")
sal = float(input())
print(" Insert Job Level ")
job = float(input())
if job > 10:
    bone = 0.25
else:
    if job > 5 and job < 9:
        bone = 0.2
    else:
        bone = 0.1
bonus = sal * bone
print("The bonus for " + name + " is $" + str(bonus))
