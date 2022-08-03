from itertools import permutations


def solution(numbers):
    answer = 0
    max_num = int(''.join(sorted(list(numbers), reverse=True)))
    prime_set = set([0, 1])
    for i in range(2, int(max_num**(1/2))+1):
        if i not in prime_set:
            for j in range(i+i, max_num+1, i):
                prime_set.add(j)
    chk_num = set()
    for i in range(1, len(numbers)+1):
        for p in permutations(list(numbers), i):
            num = int(''.join(p))
            if num not in prime_set and num not in chk_num:
                answer += 1
                chk_num.add(num)
    return answer


print(solution("17"))
print(solution("011"))
