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
# Stores all player-related game data, including ending result.
player = {
    "name": "",
    "health": 100,
    "location": "road",
    "inventory": [],
    "documents": False,
    "officer_distracted": False,
    "game_over": False,
    "ending": ""  # Tracks which ending the player achieved
}


def reset_player():
    """
    Resets all player data to its initial state.
    This allows the game to restart cleanly for a replay.
    """
    player["name"] = ""
    player["health"] = 100
    player["location"] = "road"
    player["inventory"] = []
    player["documents"] = False
    player["officer_distracted"] = False
    player["game_over"] = False
    player["ending"] = ""

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


def safehouse():
    """
    Preparation area. The player can gather equipment and receive
    guidance before entering more dangerous locations.
    """
    player["location"] = "safehouse"
    print("\nYou enter the resistance safehouse.")
    print("Inside, maps, radios, and supply crates fill the dim room.")

    while player["location"] == "safehouse" and not player["game_over"]:
        print("\nChoices: talk, take flashlight, take medkit, return, status")
        choice = get_choice(
            "What do you do? ",
            ["talk", "take flashlight", "take medkit", "return", "status"]
        )

        if choice == "talk":
            print("A resistance leader whispers,")
            print("'The bunker may contain the keycard needed to enter the office.'")
        elif choice == "take flashlight":
            if "flashlight" not in player["inventory"]:
                player["inventory"].append("flashlight")
                print("You take a flashlight.")
            else:
                print("You already took the flashlight.")
        elif choice == "take medkit":
            if "medkit" not in player["inventory"]:
                player["inventory"].append("medkit")
                print("You take a medkit.")
            else:
                print("You already took the medkit.")
        elif choice == "return":
            road()
        elif choice == "status":
            show_status()


def bunker():
    """
    Secondary mission area. The player can find the keycard here,
    but entering unprepared may cause damage.
    """
    player["location"] = "bunker"
    print("\nYou slip into the enemy bunker under cover of darkness.")

    # The flashlight helps the player avoid injury in the dark bunker.
    if "flashlight" not in player["inventory"]:
        print("Without a flashlight, you stumble through the dark and hit exposed metal.")
        player["health"] -= 20
        print("You lost 20 health.")

        if player["health"] <= 0:
            bad_ending_defeat()
            return

    while player["location"] == "bunker" and not player["game_over"]:
        print("\nChoices: search, use medkit, inspect, return, status")
        choice = get_choice(
            "What do you do? ",
            ["search", "use medkit", "inspect", "return", "status"]
        )

        if choice == "search":
            if "keycard" not in player["inventory"]:
                player["inventory"].append("keycard")
                print("You search a locker and find an enemy keycard.")
            else:
                print("You already found the keycard here.")
        elif choice == "use medkit":
            if "medkit" in player["inventory"]:
                player["inventory"].remove("medkit")
                player["health"] += 20
                if player["health"] > 100:
                    player["health"] = 100
                print("You use the medkit and recover 20 health.")
            else:
                print("You do not have a medkit.")
        elif choice == "inspect":
            print("You overhear that the stolen documents are still inside the ruined office.")
        elif choice == "return":
            road()
        elif choice == "status":
            show_status()


def office():
    """
    Final mission area. The player must have the keycard to enter.
    Different choices here determine the ending.
    """
    player["location"] = "office"
    print("\nYou approach the ruined enemy office.")

    # Require the keycard before allowing the player to continue.
    if "keycard" not in player["inventory"]:
        print("The locked entrance will not open. You need a keycard.")
        road()
        return

    print("You unlock the door and step inside.")
    print("The documents are on a desk, but an enemy officer notices you.")

    while player["location"] == "office" and not player["game_over"]:
        print("\nChoices: fight, distract, negotiate, take documents, status")
        choice = get_choice(
            "What do you do? ",
            ["fight", "distract", "negotiate", "take documents", "status"]
        )

        if choice == "fight":
            print("You lunge at the officer in a desperate struggle.")
            player["health"] -= 30
            print("You lost 30 health.")

            if player["health"] <= 0:
                bad_ending_defeat()
            else:
                print("You force the officer back, but the room is still dangerous.")
        elif choice == "distract":
            print("You throw debris across the room, drawing the officer's attention away.")
            player["officer_distracted"] = True
        elif choice == "negotiate":
            true_ending()
        elif choice == "take documents":
            if player["officer_distracted"]:
                player["documents"] = True
                clever_ending()
            elif player["health"] >= 70:
                player["documents"] = True
                heroic_ending()
            else:
                tragic_ending()
        elif choice == "status":
            show_status()


def heroic_ending():
    """
    Successful ending achieved through combat and high health.
    """
    print("\n" + "=" * 55)
    print("HEROIC ENDING")
    print("=" * 55)
    print(f"{player['name']} escapes with the documents after a direct confrontation.")
    print("The mission succeeds due to bravery under pressure.")
    
    player["documents"] = True          # Marks mission success
    player["ending"] = "Heroic Ending"  # Stores ending type
    player["game_over"] = True          # Stops the game loop


def clever_ending():
    """
    Successful ending achieved by distracting the officer.
    """
    print("\n" + "=" * 55)
    print("CLEVER ENDING")
    print("=" * 55)
    print(f"{player['name']} creates a distraction and retrieves the documents unnoticed.")
    print("The mission is completed through strategy and awareness.")
    
    player["documents"] = True
    player["ending"] = "Clever Ending"
    player["game_over"] = True


def true_ending():
    """
    Best ending achieved through negotiation rather than conflict.
    """
    print("\n" + "=" * 55)
    print("TRUE ENDING")
    print("=" * 55)
    print(f"{player['name']} calmly convinces the officer to stand down.")
    print("The documents are recovered without violence.")
    
    player["documents"] = True
    player["ending"] = "True Ending"
    player["game_over"] = True


def tragic_ending():
    """
    Partial success: documents are recovered, but the player is injured.
    """
    print("\n" + "=" * 55)
    print("TRAGIC ENDING")
    print("=" * 55)
    print(f"{player['name']} escapes with the documents but is seriously wounded.")
    print("The mission succeeds, but at a significant cost.")
    
    player["documents"] = True
    player["ending"] = "Tragic Ending"
    player["game_over"] = True


def bad_ending_defeat():
    """
    Failure ending triggered when the player's health reaches zero.
    """
    print("\n" + "=" * 55)
    print("MISSION FAILED")
    print("=" * 55)
    print(f"{player['name']} is unable to complete the mission.")
    print("The documents remain in enemy hands.")
    
    player["ending"] = "Mission Failed"
    player["game_over"] = True
    
def end_menu():
    """
    Displays the ending reached and asks the player whether to
    replay the game or quit. Returns True if replaying.
    """
    print("\n" + "=" * 55)
    print("GAME OVER")
    print("=" * 55)
    print(f"You reached: {player['ending']}")
    print("=" * 55)

    while True:
        # Gets the player's choice for next action
        choice = input("Type 'replay' to play again or 'quit' to exit: ").strip().lower()

        if choice == "replay":
            return True   # Restart game loop
        elif choice == "quit":
            print("\nThank you for playing Operation Midnight.")
            return False  # Exit game loop
        else:
            print("Invalid input. Please type 'replay' or 'quit'.")


def main():
    """
    Controls the full game cycle:
    - Starts the game
    - Runs gameplay
    - Displays ending
    - Repeats if player chooses replay
    """
    while True:
        reset_player()  # Clears previous game data
        intro()         # Starts introduction
        road()          # Begins main gameplay loop

        # After the game ends, ask if player wants to replay
        if not end_menu():
            break       # Exit loop if player chooses to quit


# Starts the program when the file is executed
main()