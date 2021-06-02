from collections import Counter

def solution(N, stages):
    answer = []
    now_stage = Counter(stages)
    fail_rate = [[i] for i in range(1, N+1)]
    user = len(stages)
    for i in range(1, N+1):
        if user != 0:
            fail_rate[i-1].append(now_stage[i]/user)
            user -= now_stage[i]
        else:
            fail_rate[i-1].append(0)
    for f in sorted(fail_rate, key = lambda x : (-x[1], x[0])):
        answer.append(f[0])

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))