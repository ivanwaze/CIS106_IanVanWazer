def Comptuit(code, credit):
    tuit = credit * get_credit_cost(code)
    return tuit

def get_credit_cost(code):
    if code == 'I':
        return 250
    elif code == 'O':
        return 550
    else:
        return 0

Total_tuit = 0

while True:
    user_input = input("Do you want to do this program? (Yes or No): ").lower()

    if user_input == 'no':
        break

    elif user_input == 'yes':
        name = input("Enter name: ")
        credits = int(input("Enter number of credits: "))
        code = input("Enter code (I/O): ")

        tuit = Comptuit(code, credits)

        print(f"Name: {name}, Credits: {credits}, Code: {code}, Tuition: {tuit}")

        Total_tuit += tuit

    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

print(f"\nTotal Tuition: {Total_tuit}")
