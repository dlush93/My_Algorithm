def solution(n):
    seive = [0]*2 + [1]*(n-1)
    for i in range(2, n+1):
        if seive[i] == 1:
            for j in range(i+i, n+1, i):
                seive[j] = 0
    return sum(seive)
solution(10)