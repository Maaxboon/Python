# Players, jersey numbers, player positions, and match details
players = ['Lionel', 'Mickey', 'Bruno', 'Michael', 'Martin']
jersey_numbers = {'10', '7', '8', '26', '22'}
player_position = {
    'Lionel': 'right winger', 
    'Mickey': 'left winger', 
    'Bruno':'Midfielder', 
    'Michael': 'striker', 
    'Martin': 'striker'
}
match_date_venue = ('January 10th', 'Camp Nou')

# Initial data
print("Initial Players:", players)
print("Initial Jersey Numbers:", jersey_numbers)
print("Initial Player Positions:", player_position)
print("Match Date and Venue:", match_date_venue)

# Add a new player Henry to the list using append()
players.append('Henry')
print("\nAfter adding Henry:", players)

# Remove a player Martin using remove()
players.remove('Martin')
del player_position['Martin']  # Ensure their position is also removed
print("\nAfter removing Martin:", players)

# Check if player is on the list
print("Is Mickey in players?", 'Mickey' in players)

# Add a new jersey number to the set
jersey_numbers.add('9')
print("\nAfter adding jersey number 9:", jersey_numbers)

# Check for duplicates
jersey_numbers.add('10')  # The set will remain unchanged because '10' is already there.
print("After trying to add a duplicate jersey number 10:", jersey_numbers)

# Access a position by player name
print("\nPosition of Lionel Messi:", player_position['Lionel'])

# Update player position
player_position['Lionel'] = 'forward'
print("Updated position of Lionel Messi:", player_position)

# Function to add a player and their position
def add_player(players_list, player_positions_dict, name, position):
    if name not in players_list:
        players_list.append(name)  # Add the player to the list
        player_positions_dict[name] = position  # Add the player and their position to the dictionary
        print(f"Added {name} as a {position}")
    else:
        print(f"{name} is already in the team.")

# Function to remove a player and their position
def remove_player(players_list, player_positions_dict, name):
    if name in players_list:
        players_list.remove(name)  # Remove the player from the list
    if name in player_positions_dict:
        del player_positions_dict[name]  # Remove the player and their position from the dictionary
    print(f"Removed {name} from the team")

# Add Henry as a defender
add_player(players, player_position, "Henry", "defender")

# Add Samson as a goalkeeper
add_player(players, player_position, "Samson", "goalkeeper")

# Remove Mickey from the team
remove_player(players, player_position, "Mickey")

# Print list of all players and their positions
print("\nFinal list of players and their positions:")
for player in players:
    position = player_position.get(player, "Unknown position")
    print(f"{player}: {position}")

# Check if the jersey number 10 is already assigned
print("\nIs jersey number 10 already assigned?", '10' in jersey_numbers)
