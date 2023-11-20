# Data
data = [("Fyers", 75), ("Ging", 84), ("Benny", 93), ("Astralis", 69), ("Conner", 77), ("Vance", 96), ("Xavier", 88), ("Hamilton", 52), ("Syler", 81), ("Louis", 79)]

# Function to display last name and highest/lowest scores
def display_highest_and_lowest(data):
    high_var = 0
    low_var = 999
    high_index = 0
    low_index = 0

    for i in range(len(data)):
        if data[i][1] > high_var:
            high_var = data[i][1]
            high_index = i
        if data[i][1] < low_var:
            low_var = data[i][1]
            low_index = i

    print(f"Highest Score: {data[high_index][0]} - Score: {high_var}")
    print(f"Lowest Score: {data[low_index][0]} - Score: {low_var}")

# Displaying highest and lowest scores along with the respective last names
display_highest_and_lowest(data)

