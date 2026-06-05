import random

def always_cooperate():
    return "C"

def always_defect():
    return "D"

def random_strategy():
    return random.choice(["C", "D"])

def tit_for_tat(opponent_history):
    if len(opponent_history) == 0:
        return "C"
    return opponent_history[-1]
