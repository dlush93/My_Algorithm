def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in range(len(d), 0, -1):
        if sum(d[:i]) <= budget:
            answer = i
            break
    return answer