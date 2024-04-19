import streamlit as st
import BlockSimulate


def main():
    st.title("Blockchain Electronic Voting System")

    blockchain = BlockSimulate.Blockchain()

    page = st.sidebar.radio(
        "Navigation", ["Authenticate", "Register", "Vote", "View Blockchain"]
    )

    if page == "Authenticate":
        st.header("Authenticate")
        st.write("Authentication page content goes here...")

    elif page == "Register":
        st.header("Register")
        st.write("Registration page content goes here...")

    elif page == "Vote":
        st.header("Vote")
        st.write("Voting page content goes here...")

    elif page == "View Blockchain":
        st.header("View Blockchain")
        st.write("Blockchain page content goes here...")
        for block in blockchain.chain:
            st.write("Index:", block.index)
            st.write("Transactions:", block.transactions)
            st.write("Timestamp:", block.timestamp)
            st.write("Previous Hash:", block.previous_hash)
            st.write("Nonce:", block.nonce)
            st.write("---")


if __name__ == "__main__":
    main()
