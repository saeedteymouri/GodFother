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

# Create a Streamlit app
def main():
    st.title("Character Name List App")

    # Create a table to display character names without row numbers
    df = pd.DataFrame({"Character": characters, "Name": [st.session_state.character_names[char] for char in characters]})
    
    # Create a button to assign roles
    if st.button("Assign Role"):
        assign_roles(df)

    # Display the table
    st.table(df.set_index("Character"))

    # Create input boxes for entering names
    st.header("Enter Names:")
    for char in characters:
        st.session_state.character_names[char] = st.text_input(f"{char}:", st.session_state.character_names[char])

def assign_roles(df):
    # Shuffle the characters list to assign roles randomly
    random.shuffle(characters)
    
    # Assign roles to names
    for i, char in enumerate(characters):
        df.at[i, "Character"] = char

if __name__ == "__main__":
    main()
