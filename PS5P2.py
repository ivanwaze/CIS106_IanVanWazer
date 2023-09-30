print(" Enter the quantity ")
qty = float(input())
print(" Enter the part number ")
partnum = input()
if partnum == "10" or partnum == "55":
    cpu = 1.0
else:
    if partnum == "99":
        cpu = 2.0
    else:
        if partnum == "80" or partnum == "70":
            cpu = 3.0
        else:
            cpu = 5.0
total = qty * cpu
print(" The total for your parts are $" + str(total))
