print(" Enter the principle rate of the CD ")
princ = float(input())
print(" Enter the year to maturity for the CD ")
ytm = int(input())
if princ > 100000 and ytm == 5:
    intrate = 0.06
else:
    if princ < 100000 and princ > 50000 and ytm == 10:
        intrate = 0.05
    else:
        if princ < 100000 and princ > 50000 and ytm == 5:
            intrate = 0.04
        else:
            intrate = 0.02
fyi = intrate * princ
print(" The principle amount is $" + str(princ))
print(" The interest rate is " + str(intrate) + "%")
print(" The first year interest rate on the CD is $" + str(fyi))
