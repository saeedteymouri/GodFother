import streamlit as st
import pandas as pd

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

    # Create input box for entering names
    new_name = st.text_input("Enter a Name")

    # Create a dropdown menu to select a character
    selected_character = st.selectbox("Select a Character", characters)

    # Create an "Add" button
    if st.button("Add"):
        if new_name:
            st.session_state.character_names[selected_character] = new_name

    # Create a table to display character names
    df = pd.DataFrame({"Character": characters, "Name": [st.session_state.character_names[char] for char in characters]})
    st.table(df)

if __name__ == "__main__":
    main()
