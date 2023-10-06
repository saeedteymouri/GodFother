import streamlit as st
import random

# Streamlit app title and description
st.title("Mafia Game (Godfather Scenario)")
st.write("Waiting for players...")

# Initialize variables
max_players = 13
player_count = 0
players = []
roles = []

# Player registration form
num_players = st.number_input("Number of Players", min_value=1, max_value=max_players, step=1, value=1)
player_names = st.multiselect("Enter Player Names", ["Player " + str(i) for i in range(1, max_players + 1)], [], key="player_names")
join_game = st.button("Join Game")

# Function to assign roles to players
def assign_roles():
    roles = [
        "Godfather",
        "Matador",
        "Saul Goodman",
        "Dr. Watson",
        "Leon (Professional)",
        "Kane's Fellow Citizen",
        "Constantine",
        "Nostradamus",
        "Simple Citizen",
        "Simple Citizen",
        "Simple Citizen",
    ]
    if player_count == 13:
        roles.append("Simple Mafia")
    return roles

# Handle player registration and role assignment
if join_game:
    if player_count < max_players:
        player_count += num_players
        players.extend(player_names[:num_players])

        if player_count >= 11:
            roles = assign_roles()
            st.write("Roles assigned:")
            for i, player in enumerate(players):
                st.write(f"{player}: {roles[i]}")
    else:
        st.write("Sorry, the capacity is full.")
