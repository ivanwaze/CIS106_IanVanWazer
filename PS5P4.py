print(" Enter quantity of tickets ")
qty = float(input())
if qty >= 25:
    ppt = 50
else:
    if qty > 10 and qty < 24:
        ppt = 60
    else:
        if qty > 5 and qty < 9:
            ppt = 70
        else:
            ppt = 75
total = qty * ppt
print(" The total number of tickets purchased is " + str(qty))
print(" The price per ticket is $" + str(ppt))
print(" The total amount for your purchase is $" + str(total))
