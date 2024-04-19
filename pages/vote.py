# vote.py
import streamlit as st
import BlockSimulate


def main():
    st.title("Vote")

    blockchain = BlockSimulate.Blockchain()

    # User input for voting
    candidate = st.selectbox(
        "Select Candidate", ["Candidate A", "Candidate B", "Candidate C"]
    )

    if st.button("Vote"):
        # Add the vote as a transaction to the blockchain
        blockchain.add_new_transaction(candidate)
        # Mine the block to record the vote on the blockchain
        blockchain.mine()
        st.success("Vote cast successfully!")


if __name__ == "__main__":
    main()
