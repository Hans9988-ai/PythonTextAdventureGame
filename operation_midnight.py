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
# Author note: if the commits look weird, it's because I am weird. I try to do things one by one off screen then add it into script haha.
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


def intro():
    """
    Introduces the setting, mission, and player role.
    """
    print("=" * 55)
    print("                 OPERATION MIDNIGHT")
    print("=" * 55)
    print("France, 1944.")
    print("You are a resistance courier operating behind enemy lines.")
    print("Your mission is to recover stolen military documents")
    print("from a ruined enemy office before they are moved by dawn.\n")

    player["name"] = input("Enter your name: ").strip()

    # Assign a default name if the player enters nothing.
    if player["name"] == "":
        player["name"] = "Courier"

    print(f"\nGood luck, {player['name']}. The mission begins now.\n")


def road():
    """
    Main hub area. The player can move to the safehouse, bunker,
    or final office location from here.
    """
    player["location"] = "road"
    print("\nYou stand on a dark country road outside an occupied village.")
    print("Nearby are a resistance safehouse, an enemy bunker, and a ruined office.")

    while player["location"] == "road" and not player["game_over"]:
        print("\nChoices: look, go safehouse, go bunker, go office, status")
        choice = get_choice(
            "What do you do? ",
            ["look", "go safehouse", "go bunker", "go office", "status"]
        )

        if choice == "look":
            print("You study the area and notice fresh boot prints in the mud.")
        elif choice == "go safehouse":
            safehouse()
        elif choice == "go bunker":
            bunker()
        elif choice == "go office":
            office()
        elif choice == "status":
            show_status()
