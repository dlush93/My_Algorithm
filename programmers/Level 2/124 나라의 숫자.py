def solution(n):
    answer = ''
    while n//3 != 0:
        remain = n%3
        n = n//3
        if remain in (1, 2):
            answer = str(remain) + answer
        else:
            answer = '4' + answer
        if 1 < n < 3:
            answer = str(n) + answer

    return answer
print(solution(1))