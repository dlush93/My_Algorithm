def solution(numbers):
    chk = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            chk.add(numbers[i] + numbers[j])
    answer = sorted(list(chk))
    return answer

print(solution([2,1,3,4,1]))