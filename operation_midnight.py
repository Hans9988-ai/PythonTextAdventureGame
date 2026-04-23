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