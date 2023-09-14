import streamlit as st

# Create a list of default names
default_names = [
    "The Godfather",
    "Matador",
    "Saul Goodman",
    "Dr. Watson",
    "Leon",
    "Constantine",
    "Nostradamus",
    "Citizen Kane",
    "Simple Citizen 1",
    "Simple Citizen 2",
    "Simple Citizen 3"
]

# Create a Streamlit app
def main():
    st.title("Name List App")

    # Create a sidebar with the default names
    st.sidebar.header("Names")
    selected_name = st.sidebar.selectbox("Select a Name", default_names)

    # Create an edit box for entering names
    new_name = st.text_input("Enter a Name")

    # Create a confirmation button
    if st.button("Add Name"):
        if new_name:
            st.write(f"{new_name} -------------------- {selected_name}")

    # Display the table with selected names
    st.header("Selected Names")

if __name__ == "__main__":
    main()
