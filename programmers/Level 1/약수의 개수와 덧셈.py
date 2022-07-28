def solution(left, right):
    answer = sum([-1*i if sum([1 for j in range(1, i+1) if not i%j])%2 else i for i in range(left, right+1)])
    return answer