def use_phone(num, hand, now_hand, pad):
    if num in (1, 4, 7):
        now_hand['L'] = pad[num]
        return 'L'
    elif num in (3, 6, 9):
        now_hand['R'] = pad[num]
        return 'R'
    else:
        if abs(now_hand['L'][0] - pad[num][0]) + abs(now_hand['L'][1] - pad[num][1]) <abs(
                now_hand['R'][0] - pad[num][0]) + abs(now_hand['R'][1] - pad[num][1]):
            now_hand['L'] = pad[num]
            return 'L'
        elif abs(now_hand['L'][0] - pad[num][0]) + abs(now_hand['L'][1] - pad[num][1]) > abs(
                now_hand['R'][0] - pad[num][0]) + abs(now_hand['R'][1] - pad[num][1]):
            now_hand['R'] = pad[num]
            return 'R'
        else:
            if hand == 'left':
                now_hand['L'] = pad[num]
                return 'L'
            else:
                now_hand['R'] = pad[num]
                return 'R'


def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2],
              0: [3, 1]}
    now_hand = {'L': [3, 0], 'R': [3, 2]}
    for i in numbers:
        answer += use_phone(i, hand, now_hand, keypad)

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
