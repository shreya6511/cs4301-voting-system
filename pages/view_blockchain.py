import streamlit as st
import BlockSimulate


def main():
    st.title("View Blockchain")

    blockchain = BlockSimulate.Blockchain()

    st.write("Blockchain details:")
    for block in blockchain.chain:
        st.write("Index:", block.index)
        st.write("Transactions:", block.transactions)
        st.write("Timestamp:", block.timestamp)
        st.write("Previous Hash:", block.previous_hash)
        st.write("Nonce:", block.nonce)
        st.write("---")


if __name__ == "__main__":
    main()
