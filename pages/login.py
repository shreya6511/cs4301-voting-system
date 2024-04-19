import streamlit as st
import os

# This class performs authentication of a user account
# by checking if the user and password are in the dictionary called accounts.
# This is a mock implementation for the purposes of this project
# as we do not have access to check government data.


class Accounts:
    def __init__(self):
        # holds all the registered user accounts
        self.accounts = {}
        self.load_accounts_from_file("accounts.txt")

    def load_accounts_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    username, password = line.strip().split(":")
                    self.accounts[username] = password
        except FileNotFoundError:
            print("Accounts File Not Found")

    def add_account(self, username, password):
        self.accounts[username] = password
        return True

    def perform_authentication(self, user, pw):
        # Dummy authentication logic
        if user in self.accounts.keys() and pw == self.accounts[user]:
            return True
        else:
            return False


def main():
    st.title("Blockchain Electronic Voting System")

    user_accounts = Accounts()

    # Check if the user is authenticated
    authenticated = False
    if "authenticated" in st.session_state:
        authenticated = st.session_state.authenticated

    st.header("Authenticate")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if user_accounts.perform_authentication(username, password):
            st.success("Login successful!")
            st.switch_page("pages/vote.py")
        else:
            st.error("Account Not Found")


if __name__ == "__main__":
    main()
