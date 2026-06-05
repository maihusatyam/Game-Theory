payoffs = {
    ("C","C"): (3,3),
    ("C","D"): (0,5),
    ("D","C"): (5,0),
    ("D","D"): (1,1)
}
def play_round(move_a, move_b):
    return payoffs[move_a, move_b]

def simulate(strategy1, strategy2, rounds):
    history1 = []
    history2 = []

    score1 = 0
    score2 = 0

    for _ in range(rounds):

        if strategy1.__name__ == "tit_for_tat":
            move1 = strategy1(history2)
        else:
            move1 = strategy1()

        if strategy2.__name__ == "tit_for_tat":
            move2 = strategy2(history1)
        else:
            move2 = strategy2()

        round_score1, round_score2 = play_round(move1, move2)

        score1 += round_score1
        score2 += round_score2

        history1.append(move1)
        history2.append(move2)

    return score1, score2