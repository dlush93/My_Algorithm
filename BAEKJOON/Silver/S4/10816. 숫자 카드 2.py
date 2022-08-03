N = int(input())
cards = list(map(int, input().split()))
card_dict = dict()
for card in cards:
    if card not in card_dict:
        card_dict[card] = 0
    card_dict[card] += 1

M = int(input())
num_list = list(map(int, input().split()))
for num in num_list:
    if num in card_dict:
        print(card_dict[num], end=' ')
    else:
        print(0, end=' ')