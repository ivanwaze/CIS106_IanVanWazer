def CompMPG(miles, gals):
    return miles / gals

count = 0

while True:
    user_input = input("Do you want to do this program? (Yes or No): ").lower()

    if user_input == 'no':
        break

    elif user_input == 'yes':
        city = input("Enter city: ")
        miles = float(input("Enter number of miles driven: "))
        gals = float(input("Enter number of gallons used: "))

        MPG = CompMPG(miles, gals)

        print(f"City: {city}, Miles: {miles}, Gallons: {gals}, MPG: {MPG}")

        count += 1

    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

print(f"\nTotal Count: {count}")
