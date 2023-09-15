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

# Initialize Godfather's and Matador's abilities and victims for each night
for night in range(1, 3):
    if f'godfather_ability_{night}' not in st.session_state:
        st.session_state[f'godfather_ability_{night}'] = "doesn't kill anyone"

    if f'godfather_victim_{night}' not in st.session_state:
        st.session_state[f'godfather_victim_{night}'] = ""

    if f'matador_victim_{night}' not in st.session_state:
        st.session_state[f'matador_victim_{night}'] = ""

# Initialize a list to store the results of each night
if 'night_results' not in st.session_state:
    st.session_state.night_results = []

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

    # Section for each night
    for night in range(1, 3):
        st.header(f"During the Night {night}")
        st.subheader(f"The Role of the Godfather {night}")
        godfather_ability = st.selectbox(f"Choose Godfather's Ability (Night {night}):", ["doesn't kill anyone", "kills", "slaughters"])
        st.session_state[f'godfather_ability_{night}'] = godfather_ability
        godfather_victim = st.text_input(f"Enter Victim's Name (if applicable) (Night {night}):")
        st.session_state[f'godfather_victim_{night}'] = godfather_victim

        st.subheader(f"The Role of the Matador {night}")
        matador_victim = st.text_input(f"Enter Matador's Target's Name (if applicable) (Night {night}):")
        st.session_state[f'matador_victim_{night}'] = matador_victim

        # Button to display ability actions for the current night
        if st.button(f"Ability Actions {night}"):
            night_results = display_ability_actions(night)
            st.write(night_results)  # Display and record night results

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
        night_actions += f"The Godfather {night} doesn't kill anyone during the night."
    elif godfather_ability == "kills":
        if godfather_victim:
            night_actions += f"The Godfather {night} kills {godfather_victim} during the night."
        else:
            night_actions += f"The Godfather {night} kills someone during the night."
    elif godfather_ability == "slaughters":
        if godfather_victim:
            night_actions += f"The Godfather {night} slaughters {godfather_victim} during the night."
        else:
            night_actions += f"The Godfather {night} slaughters someone during the night."

    night_actions += f"\n{matador_ability_message}"

    # Append night actions to the list of night results
    st.session_state.night_results.append(night_actions)

    return night_actions

if __name__ == "__main__":
    main()
