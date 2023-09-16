import streamlit as st
import pandas as pd
import random

# Create a list of characters
characters = [
    "Godfather", "Matador", "Saul Goodman", "Dr. Watson", "Leon",
    "Constantine", "Nostradamus", "Citizen Kane", "Simple Citizen 1",
    "Simple Citizen 2", "Simple Citizen 3"
]

# Define the sides associated with characters
character_sides = {
    "Godfather": "Mafia",
    "Matador": "Mafia",
    "Saul Goodman": "Mafia",
    "Dr. Watson": "Citizen",
    "Leon": "Citizen",
    "Constantine": "Citizen",
    "Nostradamus": "Independent",
    "Citizen Kane": "Citizen",
    "Simple Citizen 1": "Citizen",
    "Simple Citizen 2": "Citizen",
    "Simple Citizen 3": "Citizen"
}

# Initialize a dictionary to store names for each character
if 'character_names' not in st.session_state:
    st.session_state.character_names = {char: "" for char in characters}

# Initialize a dictionary to store night-specific data
if 'night_data' not in st.session_state:
    st.session_state.night_data = {}

# Initialize a dictionary to store Dr. Watson's saved person every night
if 'doctor_saved' not in st.session_state:
    st.session_state.doctor_saved = {}

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

    # Display the table of names and roles
    if any(st.session_state.character_names.values()):
        df = pd.DataFrame({"Character": characters, "Name": [st.session_state.character_names[char] for char in characters]})
        st.table(df.set_index("Character"))

    # Input box for entering a person's name
    person_name = st.text_input("Enter Person's Name:")
    if st.button("Show Person's Role"):
        show_person_role(person_name)

    # Section for each night
    for night in range(1, 9):
        display_night_section(night)

def assign_roles():
    # Shuffle the names list to randomize the names
    names = list(st.session_state.character_names.values())
    random.shuffle(names)

    # Assign randomized names to the table
    df = pd.DataFrame({"Character": characters, "Name": names})
    st.session_state.character_names = {char: name for char, name in zip(characters, names)}

def get_person_role_by_name(person_name):
    person_role = ""
    for char, name in st.session_state.character_names.items():
        if name.lower() == person_name.lower():
            person_role = char
            break
    return person_role

def show_person_role(person_name):
    person_role = get_person_role_by_name(person_name)
    st.write(f"{person_name}'s role is {person_role} ({character_sides.get(person_role)})")

def display_night_section(night):
    st.header(f"During the Night {night}")

    # Create input box for Dr. Watson to save a person's name
    saved_person = st.text_input(f"Enter Person's Name to Save (if applicable) (Night {night}):")

    godfather_ability = st.selectbox(f"Choose Godfather's Ability (Night {night}):", ["doesn't kill anyone", "kills", "slaughters", "bribery"])
    
    # Display different input boxes based on Godfather's ability
    if godfather_ability == "kills":
        godfather_victim = st.text_input(f"Enter Victim's Name (if applicable) (Night {night}):")
    elif godfather_ability == "bribery":
        bribery_target = st.text_input(f"Enter Target's Name for Bribery (if applicable) (Night {night}):")
    
    matador_victim = st.text_input(f"Enter Matador's Target's Name (if applicable) (Night {night}):")

    # Button to display night results for the current night
    if st.button(f"Night Result {night}"):
        night_data = {
            "Godfather Ability": godfather_ability,
            "Godfather Victim": godfather_victim if godfather_ability == "kills" else "",
            "Bribery Target": bribery_target if godfather_ability == "bribery" else "",
            "Matador Victim": matador_victim
        }

        # Store night-specific data
        st.session_state.night_data[night] = night_data
        st.session_state.doctor_saved[night] = saved_person

        display_night_results(night)

def display_night_results(night):
    night_data = st.session_state.night_data.get(night, {})
    godfather_ability = night_data.get("Godfather Ability", "doesn't kill anyone")
    godfather_victim = night_data.get("Godfather Victim", "")
    bribery_target = night_data.get("Bribery Target", "")
    matador_victim = night_data.get("Matador Victim", "")
    doctor_saved = st.session_state.doctor_saved.get(night, "")
    matador_ability_message = f"The Matador took the ability of {matador_victim} ({get_person_role_by_name(matador_victim)}), who cannot use their ability." if matador_victim else ""
    bribery_message = f"The Godfather used bribery on {bribery_target} ({get_person_role_by_name(bribery_target)})." if bribery_target else ""

    night_actions = ""

    if godfather_ability == "doesn't kill anyone":
        night_actions += f"The Godfather {night} doesn't kill anyone during the night."
    elif godfather_ability == "kills":
        if godfather_victim:
            character_name = st.session_state.character_names.get(godfather_victim, godfather_victim)
            character_role = get_person_role_by_name(character_name)
            if character_role == "Citizen" and godfather_victim == "Leon":
                night_actions += f"The Godfather {night} shot {character_name} ({character_sides.get(character_role)}) with an arrow, but {character_name}'s armor was destroyed, and he himself survived."
            else:
                night_actions += f"The Godfather {night} kills {character_name} ({character_sides.get(character_role)}) during the night."
        else:
            night_actions += f"The Godfather {night} kills someone during the night."
    elif godfather_ability == "slaughters":
        if godfather_victim:
            character_name = st.session_state.character_names.get(godfather_victim, godfather_victim)
            character_role = character_sides.get(godfather_victim)
            if character_role == "Citizen" and godfather_victim == "Leon":
                night_actions += f"The Godfather {night} shot {character_name} ({character_sides.get(character_role)}) with an arrow, but {character_name}'s armor was destroyed, and he himself survived."
            else:
                night_actions += f"The Godfather {night} slaughters {character_name} ({character_sides.get(character_role)}) during the night."
        else:
            night_actions += f"The Godfather {night} slaughters someone during the night."
    elif godfather_ability == "bribery":
        if bribery_target:
            night_actions += bribery_message

    if doctor_saved:
        night_actions += f" Dr. Watson saved {doctor_saved} ({character_sides.get(get_person_role_by_name(doctor_saved))})."

    night_actions += f"\n{matador_ability_message}"

    st.write(night_actions)

if __name__ == "__main__":
    main()
