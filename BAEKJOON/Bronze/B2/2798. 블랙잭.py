import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
result = 0
for card in combinations(cards, 3):
    if result < sum(card) < M:
        result = sum(card)
    elif sum(card) == M:
        result = sum(card)
        break
print(result)