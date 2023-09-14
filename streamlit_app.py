import streamlit as st
import pandas as pd
import random

# Create a Streamlit app
def main():
    st.title("Character Name List App")

    # Ask the user for the number of players
    num_players = st.selectbox("Select the Number of Players", list(range(11, 14)))

    # Create a list of characters based on the selected number of players
    characters = [
        "Godfather", "Matador", "Saul Goodman", "Dr. Watson", "Leon",
        "Constantine", "Nostradamus", "Citizen Kane", "Simple Citizen 1",
        "Simple Citizen 2", "Simple Citizen 3"
    ]

    if num_players >= 12:
        characters.append("Simple Citizen 4")
    if num_players == 13:
        characters.append("Simple Mafia")

    # Initialize a dictionary to store names for each character
    if 'character_names' not in st.session_state:
        st.session_state.character_names = {char: "" for char in characters}

    # Create input boxes for entering names with labels "Person 1" to "Person n"
    st.header("Enter Names:")
    for i, char in enumerate(characters):
        st.session_state.character_names[char] = st.text_input(f"Person {i+1}:", st.session_state.character_names[char])

    # Create a button to assign roles
    if st.button("Assign Role"):
        assign_roles(characters)

    # Display the table only after assigning roles
    if any(st.session_state.character_names.values()):
        df = pd.DataFrame({"Character": characters, "Name": [st.session_state.character_names[char] for char in characters]})
        st.table(df.set_index("Character"))

def assign_roles(characters):
    # Shuffle the names list to randomize the names
    names = list(st.session_state.character_names.values())
    random.shuffle(names)

    # Assign randomized names to the table
    df = pd.DataFrame({"Character": characters, "Name": names})
    st.session_state.character_names = {char: name for char, name in zip(characters, names)}

if __name__ == "__main__":
    main()
