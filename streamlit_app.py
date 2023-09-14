import streamlit as st
# Create a list to store the names
names = []

# Use a for loop to prompt the user for 11 names
for i in range(1, 12):
    name = input(f"Enter name {i}: ")
    names.append(name)

# Print the collected names
print("You entered the following names:")
for name in names:
    print(name)
st.title("Godfother Moderator")
