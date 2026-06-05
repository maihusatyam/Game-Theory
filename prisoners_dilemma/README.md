# Prisoner's Dilemma Simulator

An interactive Prisoner's Dilemma simulator built with Python and Streamlit. This project explores one of the most famous problems in game theory by allowing users to simulate matches between different strategies and analyze their performance through tournaments.

## Introduction

The Prisoner's Dilemma is a classic problem in game theory that demonstrates how rational individuals may choose actions that lead to worse outcomes for everyone involved.

In the traditional scenario, two prisoners must independently decide whether to:

* Cooperate
* Defect

Although cooperation produces a better collective outcome, each prisoner has an incentive to defect for personal gain. This conflict between individual incentives and collective welfare makes the Prisoner's Dilemma one of the most studied models in economics, political science, biology, and computer science.

This simulator allows users to experiment with different strategies and observe how they perform in repeated interactions.

---

## Features

* Interactive Streamlit interface
* Adjustable number of rounds
* Single match simulation
* Round-robin tournament mode
* Tournament leaderboard
* Score visualization with bar charts
* Classic Prisoner's Dilemma payoff matrix
* Multiple game theory strategies

---

## Implemented Strategies

### Always Cooperate

Always chooses cooperation.

```text
Move(t) = C
```

### Always Defect

Always chooses defection.

```text
Move(t) = D
```

### Random

Randomly chooses between cooperation and defection.

```text
Move(t) ∈ {C, D}
```

### Tit For Tat

* Cooperates on the first move.
* Copies the opponent's previous move afterwards.

```text
Move(1) = C

Move(t) = Opponent(t−1), for t > 1
```

Tit For Tat is one of the most famous strategies in game theory and was highly successful in Robert Axelrod's Prisoner's Dilemma tournaments.

---

## Mathematical Foundation

The Prisoner's Dilemma is defined by the following payoff matrix.

|           | Cooperate | Defect |
| --------- | --------- | ------ |
| Cooperate | (3,3)     | (0,5)  |
| Defect    | (5,0)     | (1,1)  |

The values satisfy the classic Prisoner's Dilemma condition:

```text
T > R > P > S
```

where:

* T = Temptation = 5
* R = Reward = 3
* P = Punishment = 1
* S = Sucker's Payoff = 0

Therefore:

```text
5 > 3 > 1 > 0
```

### Repeated Games

The simulator supports repeated interactions over multiple rounds.

The total score accumulated by a strategy is:

```text
Total Score = Σ Payoff(i)
```

where:

* i represents the round number
* Payoff(i) is the reward received in round i

---

## Project Structure

```text
prisoners_dilemma/
│
├── app.py
├── game.py
├── main.py
├── strategies.py
├── tournament.py
└── .gitignore
```

### File Overview

#### app.py

Contains the Streamlit user interface.

#### strategies.py

Contains implementations of all strategies.

#### game.py

Contains:

* Payoff matrix
* Round simulation logic
* Multi-round simulation engine

#### tournament.py

Runs round-robin tournaments and calculates leaderboard scores.

#### main.py

Simple command-line testing and experimentation.

---

## Installation

Install dependencies:

```bash
pip install streamlit pandas
```

---

## Running the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

---

## Example Tournament Result

```text
always_defect: 2012
tit_for_tat: 1847
random_strategy: 1783
always_cooperate: 1524
```

Results may vary because the Random strategy produces different outcomes each run.

---

## Concepts Demonstrated

* Game Theory
* Prisoner's Dilemma
* Repeated Games
* Strategic Decision Making
* Tournament Analysis
* Strategy Evaluation
* Behavioral Modeling

---
