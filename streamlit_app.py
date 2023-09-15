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

# Initialize a dictionary to store night-specific data
if 'night_data' not in st.session_state:
    st.session_state.night_data = {}

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
    display_night_section(1)

    # Section for Night 2
    display_night_section(2)

def assign_roles():
    # Shuffle the names list to randomize the names
    names = list(st.session_state.character_names.values())
    random.shuffle(names)

    # Assign randomized names to the table
    df = pd.DataFrame({"Character": characters, "Name": names})
    st.session_state.character_names = {char: name for char, name in zip(characters, names)}

def display_night_section(night):
    st.header(f"During the Night {night}")
    godfather_ability = st.selectbox(f"Choose Godfather's Ability (Night {night}):", ["doesn't kill anyone", "kills", "slaughters"])
    godfather_victim = st.text_input(f"Enter Victim's Name (if applicable) (Night {night}):")
    matador_victim = st.text_input(f"Enter Matador's Target's Name (if applicable) (Night {night}):")

    # Button to display ability actions for the current night
    if st.button(f"Apply Ability {night}"):
        night_data = {
            "Godfather Ability": godfather_ability,
            "Godfather Victim": godfather_victim,
            "Matador Victim": matador_victim
        }

        # Store night-specific data
        st.session_state.night_data[night] = night_data

        display_ability_actions(night)

def display_ability_actions(night):
    night_data = st.session_state.night_data.get(night, {})
    godfather_ability = night_data.get("Godfather Ability", "doesn't kill anyone")
    godfather_victim = night_data.get("Godfather Victim", "")
    matador_victim = night_data.get("Matador Victim", "")
    matador_ability_message = f"The Matador took the ability of {matador_victim}, who cannot use their ability." if matador_victim else ""

    night_actions = ""

    if godfather_ability == "doesn't kill anyone":
        night_actions += f"The Godfather {night} doesn't kill anyone during the night."
    elif godfather_ability == "kills":
        if godfather_victim:
            if godfather_victim == "Leon":
                night_actions += f"The Godfather {night} shot Leon with an arrow, but Leon's armor was destroyed and he himself survived."
            else:
                night_actions += f"The Godfather {night} kills {godfather_victim} during the night."
        else:
            night_actions += f"The Godfather {night} kills someone during the night."
    elif godfather_ability == "slaughters":
        if godfather_victim:
            night_actions += f"The Godfather {night} slaughters {godfather_victim} during the night."
        else:
            night_actions += f"The Godfather {night} slaughters someone during the night."

    night_actions += f"\n{matador_ability_message}"

    st.write(night_actions)

if __name__ == "__main__":
    main()
