total = 0
count = 0
print(" Do you want to continue ? (Yes or No)")
ans = input()
while ans == "Yes":
    count = count + 1
    print(" Enter last name ")
    lstnm = input()
    print(" Enter hours worked ")
    hrs = int(input())
    extrahrs = hrs - 40
    print(" Enter pay rate ")
    payrt = float(input())
    if hrs > 40:
        gross = payrt * 40 + 1.5 * payrt * extrahrs
    else:
        gross = payrt * 40
    print(" The total pay for " + lstnm + " is $" + str(gross))
    total = gross
    print(" Do you want to continue ? (Yes or No)")
    ans = input()
total = total + gross
print(" Total gross pay is " + str(total) + " total employees is " + str(count))
