import streamlit as st
import pandas as pd
import random

# Create a list of characters
characters = [
    "Godfather", "Matador", "Saul Goodman", "Dr. Watson", "Leon",
    "Constantine", "Nostradamus", "Citizen Kane", "Simple Citizen 1",
    "Simple Citizen 2", "Simple Citizen 3"
]

# Initialize a dictionary to store names for each character for Night 1 and Night 2
if 'character_names_1' not in st.session_state:
    st.session_state.character_names_1 = {char: "" for char in characters}

if 'character_names_2' not in st.session_state:
    st.session_state.character_names_2 = {char: "" for char in characters}

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

# Create a Streamlit app
def main():
    st.title("Character Name List App")

    # Create input boxes for entering names with labels "Person 1" to "Person 11" for Night 1
    st.header("Enter Names (Night 1):")
    for i, char in enumerate(characters):
        st.session_state.character_names_1[char] = st.text_input(f"Person {i+1} (Night 1):", st.session_state.character_names_1[char], key=f"char_name_1_{i}")

    # Create a button to assign roles for Night 1
    if st.button("Assign Role (Night 1)"):
        assign_roles(1)

    # Display the table for Night 1 only after assigning roles
    if any(st.session_state.character_names_1.values()):
        df = pd.DataFrame({"Character": characters, "Name": [st.session_state.character_names_1[char] for char in characters]})
        st.table(df.set_index("Character"))

    # Section for Night 1
    st.header("During the Night 1")
    st.subheader("The Role of the Godfather 1")
    godfather_ability_1 = st.selectbox("Choose Godfather's Ability (Night 1):", ["doesn't kill anyone", "kills", "slaughters"], key="godfather_ability_1")
    st.session_state.godfather_ability_1 = godfather_ability_1
    godfather_victim_1 = st.text_input("Enter Victim's Name (if applicable) (Night 1):", key="godfather_victim_1")
    st.session_state.godfather_victim_1 = godfather_victim_1

    st.subheader("The Role of the Matador 1")
    matador_victim_1 = st.text_input("Enter Matador's Target's Name (if applicable) (Night 1):", key="matador_victim_1")
    st.session_state.matador_victim_1 = matador_victim_1

    # Button to display ability actions for Night 1
    if st.button("Ability Actions 1"):
        display_ability_actions(1)

    # Create input boxes for entering names with labels "Person 1" to "Person 11" for Night 2
    st.header("Enter Names (Night 2):")
    for i, char in enumerate(characters):
        st.session_state.character_names_2[char] = st.text_input(f"Person {i+1} (Night 2):", st.session_state.character_names_2[char], key=f"char_name_2_{i}")

    # Create a button to assign roles for Night 2
    if st.button("Assign Role (Night 2)"):
        assign_roles(2)

    # Display the table for Night 2 only after assigning roles
    if any(st.session_state.character_names_2.values()):
        df = pd.DataFrame({"Character": characters, "Name": [st.session_state.character_names_2[char] for char in characters]})
        st.table(df.set_index("Character"))

    # Section for Night 2
    st.header("During the Night 2")
    st.subheader("The Role of the Godfather 2")
    godfather_ability_2 = st.selectbox("Choose Godfather's Ability (Night 2):", ["doesn't kill anyone", "kills", "slaughters"], key="godfather_ability_2")
    st.session_state.godfather_ability_2 = godfather_ability_2
    godfather_victim_2 = st.text_input("Enter Victim's Name (if applicable) (Night 2):", key="godfather_victim_2")
    st.session_state.godfather_victim_2 = godfather_victim_2

    st.subheader("The Role of the Matador 2")
    matador_victim_2 = st.text_input("Enter Matador's Target's Name (if applicable) (Night 2):", key="matador_victim_2")
    st.session_state.matador_victim_2 = matador_victim_2

    # Button to display ability actions for Night 2
    if st.button("Ability Actions 2"):
        display_ability_actions(2)

def assign_roles(night):
    # Shuffle the names list to randomize the names for the specified night
    if night == 1:
        names = list(st.session_state.character_names_1.values())
    else:
        names = list(st.session_state.character_names_2.values())
    random.shuffle(names)

    # Assign randomized names to the table for the specified night
    df = pd.DataFrame({"Character": characters, "Name": names})
    if night == 1:
        st.session_state.character_names_1 = {char: name for char, name in zip(characters, names)}
    else:
        st.session_state.character_names_2 = {char: name for char, name in zip(characters, names)}

def display_ability_actions(night):
    if night == 1:
        godfather_ability = st.session_state.godfather_ability_1
        godfather_victim = st.session_state.godfather_victim_1
        matador_ability_message = ""
        matador_victim = st.session_state.matador_victim_1
    else:
        godfather_ability = st.session_state.godfather_ability_2
        godfather_victim = st.session_state.godfather_victim_2
        matador_ability_message = ""
        matador_victim = st.session_state.matador_victim_2

    if matador_victim:
        matador_ability_message = f"The Matador took the ability of {matador_victim}, who cannot use their ability."

    if godfather_ability == "doesn't kill anyone":
        st.write("The Godfather doesn't kill anyone during the night.")
    elif godfather_ability == "kills":
        if godfather_victim:
            st.write(f"The Godfather kills {godfather_victim} during the night.")
        else:
            st.write("The Godfather kills someone during the night.")
    elif godfather_ability == "slaughters":
        if godfather_victim:
            st.write(f"The Godfather slaughters {godfather_victim} during the night.")
        else:
            st.write("The Godfather slaughters someone during the night.")

    st.write(matador_ability_message)

if __name__ == "__main__":
    main()
