def display_night_results(night):
    night_data = st.session_state.night_data.get(night, {})
    godfather_ability = night_data.get("Godfather Ability", "doesn't kill anyone")
    godfather_victim = night_data.get("Godfather Victim", "")
    matador_victim = night_data.get("Matador Victim", "")
    matador_ability_message = ""

    if matador_victim:
        matador_role = get_person_role_by_name(matador_victim)
        matador_ability_message = f"The Matador ({matador_role}) took the ability of {matador_victim}, who cannot use their ability."

    night_actions = ""

    if godfather_ability == "doesn't kill anyone":
        night_actions += f"The Godfather {night} doesn't kill anyone during the night."
    elif godfather_ability == "kills":
        if godfather_victim:
            character_name = st.session_state.character_names.get(godfather_victim, godfather_victim)
            character_role = get_person_role_by_name(character_name)
            side = character_sides.get(character_role)
            if character_role == "Citizen" and godfather_victim == "Leon":
                night_actions += f"The Godfather {night} shot {character_name} ({character_role}) with an arrow, but {character_name}'s armor was destroyed, and he himself survived."
            else:
                night_actions += f"The Godfather {night} kills {character_name} ({character_role}) during the night."
        else:
            night_actions += f"The Godfather {night} kills someone during the night."
    elif godfather_ability == "slaughters":
        if godfather_victim:
            character_name = st.session_state.character_names.get(godfather_victim, godfather_victim)
            character_role = get_person_role_by_name(character_name)
            side = character_sides.get(character_role)
            if character_role == "Citizen" and godfather_victim == "Leon":
                night_actions += f"The Godfather {night} shot {character_name} ({character_role}) with an arrow, but {character_name}'s armor was destroyed, and he himself survived."
            else:
                night_actions += f"The Godfather {night} slaughters {character_name} ({character_role}) during the night."
        else:
            night_actions += f"The Godfather {night} slaughters someone during the night."

    night_actions += f"\n{matador_ability_message}"

    st.write(night_actions)
