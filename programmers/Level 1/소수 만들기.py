from itertools import combinations

def solution(nums):
    answer = 0
    combi = [sum(l) for l in combinations(nums, 3)]
    seive = [False]*2 + [True]*(max(combi)-1)

    for i in range(2, max(combi)+1):
        if seive[i]:
            for j in range(i+i, max(combi)+1, i):
                seive[j] = False
    for c in combi:
        if seive[c]:
            answer += 1
    return answer

print(solution([1,2,3,4]))