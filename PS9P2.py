def CompBatAv(hits, atbats):
    return hits / atbats

count = 0

while True:
    user_input = input("Do you want to do this program? (Yes or No): ").lower()

    if user_input == 'no':
        break

    elif user_input == 'yes':
        name = input("Enter name: ")
        hits = int(input("Enter number of hits: "))
        atbats = int(input("Enter number of at-bats: "))

        batav = CompBatAv(hits, atbats)

        print(f"Name: {name}, Hits: {hits}, At-Bats: {atbats}, Batting Average: {batav}")

        count += 1

    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

print(f"\nTotal Count: {count}")
