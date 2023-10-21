def CompExtPrice(qty, unitprice):
    extprice = qty * unitprice

    if extprice > 10000:
        discamt = extprice * 0.10
    else:
        discamt = 0

    newExtPrice = extprice - discamt

    return newExtPrice

totalExtPrice = 0

while True:
    user_input = input("Do you want to do this program? (Yes or No): ").lower()

    if user_input == 'no':
        break

    elif user_input == 'yes':
        qty = float(input("Enter quantity: "))
        price = float(input("Enter unit price: "))

        extprice = CompExtPrice(qty, price)

        print(f"Quantity: {qty}, Unit Price: {price}, Extended Price: {extprice}")

        totalExtPrice += extprice

    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

print(f"\nTotal Extended Price: {totalExtPrice}")
