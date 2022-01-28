def solution(n):
    for num in range(2, n+1):
        if n%num == 1:
            return num