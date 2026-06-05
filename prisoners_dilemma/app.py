import streamlit as st
import pandas as pd

from strategies import *
from game import simulate
from tournament import run_tournament

strategy_map = {
    "Always Cooperate": always_cooperate,
    "Always Defect": always_defect,
    "Random": random_strategy,
    "Tit For Tat": tit_for_tat
}

# Title
st.markdown(
    """
    <h1 style="
        color:#EEC134;
        border-bottom:3px solid #EEC134;
        padding-bottom:10px;
    ">
    Prisoner's Dilemma Simulator
    </h1>
    """,
    unsafe_allow_html=True
)

# Introduction
st.write(
    """
    The Prisoner's Dilemma is a famous game theory problem where two players
    choose whether to cooperate or defect. This simulator allows you to test
    different strategies and observe their long-term performance.
    """
)

st.divider()

# Single Match Simulator
st.header("🎮 Single Match Simulator")

st.write(
    """
    Select two strategies and the number of rounds to simulate.
    The chosen strategies will compete against each other repeatedly,
    and the final scores will be displayed.
    """
)

strategy1_name = st.selectbox(
    "Player 1 Strategy",
    strategy_map.keys()
)

strategy2_name = st.selectbox(
    "Player 2 Strategy",
    strategy_map.keys()
)

rounds = st.slider(
    "Number of Rounds",
    min_value=1,
    max_value=500,
    value=100
)

if st.button("Run Simulation"):

    score1, score2 = simulate(
        strategy_map[strategy1_name],
        strategy_map[strategy2_name],
        rounds
    )

    st.subheader("📊 Results")

    st.write(f"**{strategy1_name} Score:** {score1}")
    st.write(f"**{strategy2_name} Score:** {score2}")

    if score1 > score2:
        st.success(f"🏆 {strategy1_name} Wins!")
    elif score2 > score1:
        st.success(f"🏆 {strategy2_name} Wins!")
    else:
        st.info("🤝 It's a Tie!")

st.divider()

# Tournament
st.header("🏆 Tournament")

st.write(
    """
    Runs a round-robin tournament where every strategy plays against
    every other strategy. The leaderboard shows which strategy performs
    best overall.
    """
)

if st.button("Run Tournament"):

    scores = run_tournament()

    df = pd.DataFrame(
        list(scores.items()),
        columns=["Strategy", "Score"]
    )

    df.index = range(1, len(df) + 1)
    df.index.name = "Rank"

    st.subheader("🏅 Tournament Leaderboard")

    st.dataframe(df)

    st.subheader("📈 Score Comparison")

    st.bar_chart(
        df.set_index("Strategy")
    )

st.divider()

# Payoff Matrix
st.header("📚 Classic Prisoner's Dilemma Payoff Matrix")

st.markdown(
    """
| Player 1 | Player 2 | Payoff |
|-----------|-----------|---------|
| Cooperate | Cooperate | (3, 3) |
| Cooperate | Defect | (0, 5) |
| Defect | Cooperate | (5, 0) |
| Defect | Defect | (1, 1) |
"""
)

st.divider()

# Strategy Descriptions
st.header("🧠 Strategy Guide")

st.markdown(
    """
**Always Cooperate**  
- Always chooses cooperation.

**Always Defect**  
- Always chooses defection.

**Random**  
- Randomly chooses cooperation or defection.

**Tit For Tat**  
- Cooperates on the first move.
- Afterwards copies the opponent's previous move.
- One of the most famous strategies in game theory.
"""
)

st.divider()
