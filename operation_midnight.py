# ============================================================
# OPERATION MIDNIGHT
# A World War II Text Adventure Game
# By: Kevin Dowd
#
# Description:
# In this text-based game, the player takes the role of a
# resistance courier during World War II. The objective is to
# infiltrate enemy-controlled areas, recover secret documents,
# and escape safely. Player choices affect the outcome, leading
# to multiple possible endings.
#
# This program demonstrates:
# - functions
# - variables
# - lists
# - dictionaries
# - if / elif / else logic
# - user input and string handling
# ============================================================


# This dictionary stores the player's current game data.
player = {
    "name": "",
    "health": 100,
    "location": "road",
    "inventory": [],
    "documents": False,
    "officer_distracted": False,
    "game_over": False
}

# This list stores the major locations in the game.
locations = ["road", "safehouse", "bunker", "office"]


def show_status():
    """
    Displays the player's current condition, location, and items.
    This helps the player track progress throughout the game.
    """
    print("\n" + "=" * 40)
    print("MISSION STATUS")
    print("=" * 40)
    print(f"Name: {player['name']}")
    print(f"Health: {player['health']}")
    print(f"Location: {player['location'].title()}")
    print(f"Inventory: {player['inventory']}")
    print(f"Documents Recovered: {player['documents']}")
    print("=" * 40 + "\n")


def get_choice(prompt, valid_choices):
    """
    Repeatedly asks the player for input until a valid response
    is entered. This keeps inputs consistent and prevents errors.
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print("\nInvalid choice.")
            print("Please choose from:", ", ".join(valid_choices))
