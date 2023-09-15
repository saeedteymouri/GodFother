import streamlit as st
import pandas as pd
import random

# Create a list of characters
characters = [
    "Godfather", "Matador", "Saul Goodman", "Dr. Watson", "Leon",
    "Constantine", "Nostradamus", "Citizen Kane", "Simple Citizen 1",
    "Simple Citizen 2", "Simple Citizen 3"
]

# Initialize a dictionary to store names for each character
if 'character_names' not in st.session_state:
    st.session_state.character_names = {char: "" for char in characters}

# Initialize a dictionary to store roles and abilities
roles_and_abilities = {
    "Godfather": "Immune to Leon's one shot at night. Has a vest. Can decide whether to fire at night on behalf of the group. If he leaves the game, other members will shoot instead. Has the ability of the sixth sense, can guess the role of a player at night, and if correct, the player is eliminated. Can be confirmed by the moderator.",
    "Matador": "Can show any player at night to take away their ability for the night. If the shown player wakes up, they face elimination by the leader's order. Matador cannot kill a player for two consecutive nights.",
    "Saul Goodman": "Can trade and buy instead of shooting if a person leaves the mafia group. Can turn a simple citizen into a simple mafia once. The sign reveals the driver of that person's new role. If Saul chooses a non-simple citizen or Nostradamus, he faces the cross of the operator and disappears.",
    "Nostradamus": "Has armor and is immune to Godfather's or Leon's arrows.",
    "Leon": "Has armor that can withstand one attack from the Godfather. Can shoot two players, one at a time. If he shoots citizens, he dies.",
    "Dr. Watson": "Can save the life of one person every night, including mafia members or citizens. Can save his own life once during the game.",
    "Citizen Kane": "Can save the life of one person every night, including mafia members or citizens. Can save his own life once during the game.",
    "Constantine": "Can once bring back an expelled player, whether mafia, citizen, or independent. The summoned player's abilities continue without resetting."
}

# Create a Streamlit app
def main():
    st.title("Character Name List App")

    # Create input boxes for entering names with labels "Person 1" to "Person 11"
    st.header("Enter Names:")
    for i, char in enumerate(characters):
        st.session_state.character_names[char] = st.text_input(f"Person {i+1}:", st.session_state.character_names[char])

    # Create a button to assign roles
    if st.button("Assign Role"):
        assign_roles()

    # Display the table of names and roles only after assigning roles
    if any(st.session_state.character_names.values()):
        df = pd.DataFrame({"Character": characters, "Name": [st.session_state.character_names[char] for char in characters]})
        st.table(df.set_index("Character"))

    # Create a button to create a table of roles and abilities
    if st.button("Create Table of Roles and Abilities"):
        display_roles_and_abilities()

def assign_roles():
    # Shuffle the names list to randomize the names
    names = list(st.session_state.character_names.values())
    random.shuffle(names)

    # Assign randomized names to the table
    df = pd.DataFrame({"Character": characters, "Name": names})
    st.session_state.character_names = {char: name for char, name in zip(characters, names)}

def display_roles_and_abilities():
    # Create a table to display roles and abilities
    df = pd.DataFrame({"Role": list(roles_and_abilities.keys()), "Ability": list(roles_and_abilities.values())})
    st.table(df.set_index("Role"))

if __name__ == "__main__":
    main()
