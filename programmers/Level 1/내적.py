def solution(a, b):
    answer = 0
    for A, B in zip(a, b):
        answer += A*B
    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))