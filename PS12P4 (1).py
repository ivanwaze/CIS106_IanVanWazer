# Data
player_names = ["Swanson", "Hoerner", "Happ", "Suzuki", "Bellinger", "Ohtani", "Wisdom", "Gomes", "Tauchman", "Madrigal"]
batting_averages = [0.244, 0.283, 0.248, 0.285, 0.307, 0.304, 0.205, 0.267, 0.252, 0.263]

# Function to display player names and batting averages
def display_player_stats(names, averages):
    print("Player Names and Batting Averages:")
    for i in range(len(names)):
        print(f"{names[i]} - Batting Average: {averages[i]}")

# Function to search for a last name in the array and display stats
def search_last_name(last_name, names, averages):
    found = False
    for i in range(len(names)):
        if names[i].lower() == last_name.lower():
            print(f"Player found - {names[i]} - Batting Average: {averages[i]}")
            found = True
            break
    if not found:
        print("Player not found.")

# Displaying player names and batting averages
display_player_stats(player_names, batting_averages)

# Asking the user for a last name and searching for it
while True:
    search_name = input("\nEnter a last name to search (or 'exit' to quit): ")
    if search_name.lower() == 'exit':
        break
    search_last_name(search_name, player_names, batting_averages)
