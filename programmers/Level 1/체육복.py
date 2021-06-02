def solution(n, lost, reserve):
    reserve_possible = list(set(reserve) - set(lost))
    no_wear = list(set(lost) - set(reserve))
    answer = n - len(no_wear)
    for n in no_wear:
        if n-1 in reserve_possible:
            answer += 1
            reserve_possible.remove(n-1)
        elif n+1 in reserve_possible:
            answer += 1
            reserve_possible.remove(n+1)
    return answer

print(solution(5, [2, 4], [3]))