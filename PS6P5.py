grandtotal = 0
print(" Do you want to continue ? (Yes or No)")
ans = input()
while ans == "Yes":
    print(" Enter quantity ")
    qty = float(input())
    print(" Enter the price per item ")
    price = float(input())
    ext = qty * price
    if ext >= 10000:
        disc = 0.25
    else:
        disc = 0.1
    discamt = disc * ext
    total = ext - discamt
    print(" Quantity is " + str(qty) + " price per item is $" + str(price))
    print(" The total discount for your purchase is $" + str(discamt) + " with a discount of " + str(disc) + "%")
    print(" Your total is $" + str(total))
    print(" Do you want to continue ? (Yes or No)")
    ans = input()
grandtotal = grandtotal + total
print(" Grand total of all purchases is $" + str(grandtotal))
