def solution(lottos, win_nums):
    answer = []
    zero = 0
    for i in lottos:
        if i == 0:
            zero += 1
    match = [len(set(lottos) & set(win_nums)) + zero, len(set(lottos) & set(win_nums))]
    for m in match:
        if 7 - m < 6:
            answer.append(7-m)
        else:
            answer.append(6)
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))