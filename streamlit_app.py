import streamlit as st

# Create a dictionary with default roles and names
default_data = {
    "The Godfather": "",
    "Matador": "",
    "Saul Goodman": "",
    "Dr. Watson": "",
    "Leon": "",
    "Constantine": "",
    "Nostradamus": "",
    "Citizen Kane": "",
    "Simple Citizen 1": "",
    "Simple Citizen 2": "",
    "Simple Citizen 3": ""
}

# Create a Streamlit app
def main():
    st.title("Name List App")

    # Create a sidebar with the default roles
    st.sidebar.header("Roles")
    selected_role = st.sidebar.selectbox("Select a Role", list(default_data.keys()))

    # Create an edit box for entering names
    new_name = st.text_input("Enter a Name")

    # Create a confirmation button
    if st.button("Add Name"):
        if new_name:
            default_data[selected_role] = new_name

    # Display the table with roles and names
    st.header("Roles and Names")
    data = {"Role": list(default_data.keys()), "Name": list(default_data.values())}
    st.table(data)

if __name__ == "__main__":
    main()
