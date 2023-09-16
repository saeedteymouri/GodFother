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
    st.session_state.night_data = {night: {} for night in range(1, 9)}

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

    # Night Sections
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
    person_side = character_sides.get(person_role)
    st.write(f"{person_name}'s role is {person_role} ({person_side})")

def display_night_section(night):
    st.header(f"Night {night} Actions:")
    
    godfather_ability = st.selectbox(f"Godfather's Ability (Night {night}):", ["doesn't kill anyone", "kills", "slaughters"])
    godfather_victim = st.text_input(f"Enter Godfather's Victim (if applicable) (Night {night}):")
    matador_target = st.text_input(f"Enter Matador's Target (if applicable) (Night {night}):")
    
    if st.button(f"Announce Night {night} Results"):
        night_data = {
            "Godfather Ability": godfather_ability,
            "Godfather Victim": godfather_victim,
            "Matador Target": matador_target,
        }
        st.session_state.night_data[night] = night_data
        display_night_results(night)

def display_night_results(night):
    night_data = st.session_state.night_data.get(night, {})
    godfather_ability = night_data.get("Godfather Ability", "doesn't kill anyone")
    godfather_victim = night_data.get("Godfather Victim", "")
    matador_target = night_data.get("Matador Target", "")
    
    night_message = f"Night {night} Actions:\n"
    
    if godfather_ability == "doesn't kill anyone":
        night_message += "The Godfather didn't kill anyone during the night."
    elif godfather_ability == "kills":
        if godfather_victim:
            character_name = st.session_state.character_names.get(godfather_victim, godfather_victim)
            character_role = get_person_role_by_name(character_name)
            night_message += f"The Godfather killed {character_name} ({character_role}) during the night."
        else:
            night_message += "The Godfather killed someone during the night."
    elif godfather_ability == "slaughters":
        if godfather_victim:
            character_name = st.session_state.character_names.get(godfather_victim, godfather_victim)
            character_role = character_sides.get(godfather_victim)
            night_message += f"The Godfather slaughtered {character_name} ({character_role}) during the night."
        else:
            night_message += "The Godfather slaughtered someone during the night."
    
    if matador_target:
        night_message += f" The Matador targeted {matador_target} ({get_person_role_by_name(matador_target)}), incapacitating them for the night."
    
    st.write(night_message)

if __name__ == "__main__":
    main()
