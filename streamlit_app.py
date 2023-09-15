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

# Initialize Godfather's ability and victim
if 'godfather_ability' not in st.session_state:
    st.session_state.godfather_ability = "doesn't kill anyone"

if 'godfather_victim' not in st.session_state:
    st.session_state.godfather_victim = ""

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

    # Section for Godfather's ability
    st.header("During the Night 1")
    st.subheader("The Role of the Godfather")
    godfather_ability = st.selectbox("Choose Godfather's Ability:", ["doesn't kill anyone", "kills", "slaughters"])
    st.session_state.godfather_ability = godfather_ability
    godfather_victim = st.text_input("Enter Victim's Name (if applicable):")
    st.session_state.godfather_victim = godfather_victim

    # Button to display ability actions
    if st.button("Ability Actions"):
        display_ability_actions()

def assign_roles():
    # Shuffle the names list to randomize the names
    names = list(st.session_state.character_names.values())
    random.shuffle(names)

    # Assign randomized names to the table
    df = pd.DataFrame({"Character": characters, "Name": names})
    st.session_state.character_names = {char: name for char, name in zip(characters, names)}

def display_ability_actions():
    godfather_ability = st.session_state.godfather_ability
    godfather_victim = st.session_state.godfather_victim

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

if __name__ == "__main__":
    main()
