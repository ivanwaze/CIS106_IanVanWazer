print(" Insert quantity of widgets ")
qty = float(input())
if qty > 10000:
    price = 10
else:
    if qty < 5000:
        price = 30
    else:
        price = 20
ext = qty * price
tax = 0.07 * ext
total = tax + ext
print(" Your extended price is $" + str(ext))
print(" The tax on your purchase is $" + str(tax))
print(" The total for you today is $" + str(total))
