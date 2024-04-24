import streamlit as st
import BlockSimulate
import plotly.graph_objects as go

def main():
    st.title("View Blockchain")

    blockchain = BlockSimulate.Blockchain()
    votes = BlockSimulate.votesDict

    st.write("Blockchain details:")
    

    for i, v in enumerate(list(votes.values())):
        if v > 0:
            cand = list(votes.keys())
            blockchain.create_genesis_block()
            for j in range(v):
                blockchain.add_new_transaction("Voted for " + cand[i])
                blockchain.mine()
    
    t = []
    for block in blockchain.chain:
        for transaction in block.transactions:
            t.append(transaction)
    
    for i, block in enumerate(blockchain.chain):
        st.write("Index:", block.index)
        st.write("Transactions:", t[:i])
        st.write("Timestamp:", block.timestamp)
        st.write("Previous Hash:", block.previous_hash)
        st.write("Nonce:", block.nonce)
        st.write("---")
  
    

    
    fig = go.Figure(data=[go.Bar(
                x=list(votes.keys()), y=list(votes.values()),
                text=list(votes.values()),
                textposition='auto',
            )])
    fig.update_layout(
        title="Votes",
        yaxis_title="Number of Votes",
        font=dict(
            family="Calbri, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )

    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.8)
    fig.update_yaxes(ticks="outside", tickwidth=2, tickcolor='blue', ticklen=10)
    fig.update_yaxes(tick0=0, dtick=1)
    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
