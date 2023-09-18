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
    st.write(f"{person_name}'s role is {person_role} ({character_sides.get(person_role)})")

def display_night_section(night):
    st.header(f"During the Night {night}")

    # Godfather Section
    st.subheader(f"The Role of the Godfather {night}")
    godfather_ability = st.selectbox(f"Choose Godfather's Ability (Night {night}):", ["doesn't kill anyone", "kills", "slaughters", "bribery"])
    godfather_victim = st.text_input(f"Enter Victim's Name (if applicable) (Night {night}):")

    # Matador Section
    st.subheader(f"The Role of the Matador {night}")
    matador_target = st.text_input(f"Enter Matador's Target's Name (if applicable) (Night {night}):")

    # Doctor Watson Section
    st.subheader(f"The Role of Dr. Watson {night}")
    doctor_save = st.text_input(f"Enter the name Dr. Watson saved (if applicable) (Night {night}):")

    # Leon Section
    st.subheader(f"The Role of Leon {night}")
    leon_target = st.text_input(f"Enter Leon's Target's Name (if applicable) (Night {night}):")

    # Citizen Kane Section
    st.subheader(f"The Role of Citizen Kane {night}")
    kane_inquiry = st.text_input(f"Enter the name Citizen Kane inquires about (if applicable) (Night {night}):")

    # Constantine Section
    st.subheader(f"The Role of Constantine {night}")
    constantine_resurrect = st.text_input(f"Enter the name Constantine resurrects (if applicable) (Night {night}):")

    # Button to display night results for the current night
    if st.button(f"Announce Night {night} Results"):
        night_data = {
            "Godfather Ability": godfather_ability,
            "Godfather Victim": godfather_victim,
            "Matador Target": matador_target,
            "Doctor Save": doctor_save,
            "Leon Target": leon_target,
            "Kane Inquiry": kane_inquiry,
            "Constantine Resurrect": constantine_resurrect
        }

        # Store night-specific data
        st.session_state.night_data[night] = night_data

        display_night_results(night)

def display_night_results(night):
    night_data = st.session_state.night_data.get(night, {})
    godfather_ability = night_data.get("Godfather Ability", "doesn't kill anyone")
    godfather_victim = night_data.get("Godfather Victim", "")
    matador_target = night_data.get("Matador Target", "")
    doctor_save = night_data.get("Doctor Save", "")
    leon_target = night_data.get("Leon Target", "")
    kane_inquiry = night_data.get("Kane Inquiry", "")
    constantine_resurrect = night_data.get("Constantine Resurrect", "")

    night_actions = []

    # Godfather Actions
    if godfather_ability == "doesn't kill anyone":
        night_actions.append(f"The Godfather {night} doesn't kill anyone during the night.")
    elif godfather_ability == "kills":
        if godfather_victim:
            character_name = st.session_state.character_names.get(godfather_victim, godfather_victim)
            character_role = get_person_role_by_name(character_name)
            if character_role == "Citizen" and godfather_victim == "Leon":
                night_actions.append(f"The Godfather {night} shot {character_name} ({character_role}) with an arrow, but {character_name}'s armor was destroyed, and he himself survived.")
            else:
                night_actions.append(f"The Godfather {night} kills {character_name} ({character_role}) during the night.")
        else:
            night_actions.append(f"The Godfather {night} kills someone during the night.")
    elif godfather_ability == "slaughters":
        if godfather_victim:
            character_name = st.session_state.character_names.get(godfather_victim, godfather_victim)
            character_role = character_sides.get(godfather_victim)
            if character_role == "Citizen" and godfather_victim == "Leon":
                night_actions.append(f"The Godfather {night} shot {character_name} ({character_role}) with an arrow, but {character_name}'s armor was destroyed, and he himself survived.")
            else:
                night_actions.append(f"The Godfather {night} slaughters {character_name} ({character_role}) during the night.")
        else:
            night_actions.append(f"The Godfather {night} slaughters someone during the night.")
    
    # Matador Action
    if matador_target:
        matador_target_role = get_person_role_by_name(matador_target)
        if matador_target_role == "Simple Citizen":
            night_actions.append(f"The Matador took the ability of {matador_target} ({matador_target_role}), who cannot use their ability.")

    # Doctor Watson Action
    if doctor_save:
        doctor_save_role = get_person_role_by_name(doctor_save)
        night_actions.append(f"Dr. Watson saved {doctor_save} ({doctor_save_role}) from being targeted.")

    # Leon Action
    if leon_target:
        leon_target_role = get_person_role_by_name(leon_target)
        night_actions.append(f"Leon shot {leon_target} ({leon_target_role}) during the night.")

    # Citizen Kane Action
    if kane_inquiry:
        kane_inquiry_role = get_person_role_by_name(kane_inquiry)
        night_actions.append(f"Citizen Kane inquired about {kane_inquiry} ({kane_inquiry_role}) during the night.")

    # Constantine Action
    if constantine_resurrect:
        constantine_resurrect_role = get_person_role_by_name(constantine_resurrect)
        night_actions.append(f"Constantine resurrected {constantine_resurrect} ({constantine_resurrect_role}) during the night.")

    night_result_message = "\n".join(night_actions)
    st.write(f"Night {night} Results:")
    st.write(night_result_message)

if __name__ == "__main__":
    main()
