from strategies import *
from game import simulate

print(simulate(always_cooperate, always_cooperate, 100))
print(simulate(always_defect, always_defect, 100))
print(simulate(random_strategy, random_strategy, 100))

print(simulate(tit_for_tat, always_defect, 100))
print(simulate(tit_for_tat, random_strategy, 100))
print(simulate(tit_for_tat, tit_for_tat, 100))