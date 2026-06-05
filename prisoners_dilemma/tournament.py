from strategies import *
from game import simulate

def run_tournament():
    strategies = [
        always_cooperate,
        always_defect,
        random_strategy,
        tit_for_tat
    ]

    scores = {}

    for strategy in strategies:
        scores[strategy.__name__] = 0

    for strategy1 in strategies:
        for strategy2 in strategies:
            score1, score2 = simulate(strategy1, strategy2, 100)

            scores[strategy1.__name__] += score1
            scores[strategy2.__name__] += score2

    scores = dict(
        sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

    return scores
