count = 0
print(" Do you want to continue ? (Yes or No)")
ans = input()
while ans == "Yes":
    count = count + 1
    print(" Enter student last name ")
    lstnm = input()
    print(" Enter first exam score ")
    exam1 = float(input())
    print(" Enter second exam score ")
    exam2 = float(input())
    avg = (exam1 + exam2) / 2
    print(" The average exam score for " + lstnm + " is " + str(avg) + "%")
    print(" Do you want to continue ? (Yes or No)")
    ans = input()
print(" Total number of students is " + str(count))
