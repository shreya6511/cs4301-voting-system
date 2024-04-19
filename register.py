import streamlit as st
import pages.login as login
import os


def main():
    st.header("Register")
    st.write("Welcome to the registration page.")
    st.write("Please enter your details below to register:")
    name = st.text_input("Name")
    id_number = st.text_input("ID Number")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        user_accounts = login.Accounts()
        # Include check here that ID number matches Name by calling a governemnt issued identification system
        user_accounts.add_account(username, password)

        # Save username and password to accounts.txt
        with open("accounts.txt", "a") as f:
            f.write(f"{username}:{password}\n")

        # For demonstration purposes, let's assume registration is successful

        st.success("Registration successful!")
        st.write("You can now proceed to login.")
        st.switch_page("pages/login.py")


if __name__ == "__main__":
    main()
