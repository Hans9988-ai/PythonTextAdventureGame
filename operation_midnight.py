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
    The player succeeds through courage and strength.
    """
    print("\n" + "=" * 55)
    print("HEROIC ENDING")
    print("=" * 55)
    print(f"{player['name']} seizes the documents and escapes through the ruins.")
    print("Though the mission was dangerous, the intelligence reaches the resistance.")
    print("Your courage helps change the course of the operation.")
    player["game_over"] = True


def clever_ending():
    """
    The player succeeds by using strategy instead of force.
    """
    print("\n" + "=" * 55)
    print("CLEVER ENDING")
    print("=" * 55)
    print(f"{player['name']} uses quick thinking to distract the officer")
    print("and recover the documents without direct confrontation.")
    print("The mission is completed through intelligence and composure.")
    player["game_over"] = True


def true_ending():
    """
    The best ending. The player resolves the conflict with calm judgment.
    """
    print("\n" + "=" * 55)
    print("TRUE ENDING")
    print("=" * 55)
    print(f"{player['name']} speaks calmly and convinces the officer")
    print("that the battle is already lost and further resistance is pointless.")
    print("In a rare moment of humanity, the officer steps aside.")
    print("You leave with the documents, completing the mission without violence.")
    player["documents"] = True
    player["game_over"] = True


def tragic_ending():
    """
    A partial success ending. The player gets the documents but pays a cost.
    """
    print("\n" + "=" * 55)
    print("TRAGIC ENDING")
    print("=" * 55)
    print(f"{player['name']} manages to grab the documents,")
    print("but is wounded while escaping the office.")
    print("The mission succeeds, but at a heavy personal cost.")
    player["documents"] = True
    player["game_over"] = True


def bad_ending_defeat():
    """
    Failure ending if the player's health reaches zero.
    """
    print("\n" + "=" * 55)
    print("MISSION FAILED")
    print("=" * 55)
    print(f"{player['name']} collapses before completing the mission.")
    print("The documents remain in enemy hands.")
    player["game_over"] = True


def main():
    """
    Starts the game and sends the player into the first area.
    """
    intro()
    road()
    print("\nThank you for playing Operation Midnight.")


# This line starts the game when the file is run.
main()