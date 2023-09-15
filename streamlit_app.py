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

# Initialize Godfather's and Matador's abilities and victims for Night 1 and Night 2
if 'godfather_ability_1' not in st.session_state:
    st.session_state.godfather_ability_1 = "doesn't kill anyone"

if 'godfather_victim_1' not in st.session_state:
    st.session_state.godfather_victim_1 = ""

if 'matador_victim_1' not in st.session_state:
    st.session_state.matador_victim_1 = ""

if 'godfather_ability_2' not in st.session_state:
    st.session_state.godfather_ability_2 = "doesn't kill anyone"

if 'godfather_victim_2' not in st.session_state:
    st.session_state.godfather_victim_2 = ""

if 'matador_victim_2' not in st.session_state:
    st.session_state.matador_victim_2 = ""

# Initialize a variable to store the text for Night 1 actions
if 'night_1_actions' not in st.session_state:
    st.session_state.night_1_actions = ""

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

    # Display the table only after assigning roles
    if any(st.session_state.character_names.values()):
        df = pd.DataFrame({"Character": characters, "Name": [st.session_state.character_names[char] for char in characters]})
        st.table(df.set_index("Character"))

    # Section for Night 1
    st.header("During the Night 1")
    st.subheader("The Role of the Godfather 1")
    godfather_ability_1 = st.selectbox("Choose Godfather's Ability (Night 1):", ["doesn't kill anyone", "kills", "slaughters"])
    st.session_state.godfather_ability_1 = godfather_ability_1
    godfather_victim_1 = st.text_input("Enter Victim's Name (if applicable) (Night 1):")
    st.session_state.godfather_victim_1 = godfather_victim_1

    st.subheader("The Role of the Matador 1")
    matador_victim_1 = st.text_input("Enter Matador's Target's Name (if applicable) (Night 1):")
    st.session_state.matador_victim_1 = matador_victim_1

    # Button to display ability actions for Night 1
    if st.button("Ability Actions 1"):
        night_1_actions = display_ability_actions(1)
        st.session_state.night_1_actions = night_1_actions

    # Section for Night 2
    st.header("During the Night 2")
    st.subheader("The Role of the Godfather 2")
    godfather_ability_2 = st.selectbox("Choose Godfather's Ability (Night 2):", ["doesn't kill anyone", "kills", "slaughters"])
    st.session_state.godfather_ability_2 = godfather_ability_2
    godfather_victim_2 = st.text_input("Enter Victim's Name (if applicable) (Night 2):")
    st.session_state.godfather_victim_2 = godfather_victim_2

    st.subheader("The Role of the Matador 2")
    matador_victim_2 = st.text_input("Enter Matador's Target's Name (if applicable) (Night 2):")
    st.session_state.matador_victim_2 = matador_victim_2

    # Button to display ability actions for Night 2
    if st.button("Ability Actions 2"):
        night_1_actions = st.session_state.night_1_actions  # Retrieve Night 1 actions
        night_2_actions = display_ability_actions(2)
        st.write(night_1_actions)  # Display Night 1 actions
        st.write(night_2_actions)  # Display Night 2 actions

def assign_roles():
    # Shuffle the names list to randomize the names
    names = list(st.session_state.character_names.values())
    random.shuffle(names)

    # Assign randomized names to the table
    df = pd.DataFrame({"Character": characters, "Name": names})
    st.session_state.character_names = {char: name for char, name in zip(characters, names)}

def display_ability_actions(night):
    godfather_ability = st.session_state[f'godfather_ability_{night}']
    godfather_victim = st.session_state[f'godfather_victim_{night}']
    matador_ability_message = ""

    matador_victim = st.session_state[f'matador_victim_{night}']

    if matador_victim:
        matador_ability_message = f"The Matador took the ability of {matador_victim}, who cannot use their ability."

    night_actions = ""

    if godfather_ability == "doesn't kill anyone":
        night_actions += "The Godfather doesn't kill anyone during the night.\n"
    elif godfather_ability == "kills":
        if godfather_victim:
            night_actions += f"The Godfather kills {godfather_victim} during the night.\n"
        else:
            night_actions += "The Godfather kills someone during the night.\n"
    elif godfather_ability == "slaughters":
        if godfather_victim:
            night_actions += f"The Godfather slaughters {godfather_victim} during the night.\n"
        else:
            night_actions += "The Godfather slaughters someone during the night.\n"

    night_actions += matador_ability_message

    return night_actions

if __name__ == "__main__":
    main()
