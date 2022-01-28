from collections import Counter

def solution(grade):
    result = [1 for _ in range(len(grade))]
    grade_cnt = Counter(grade)
    for cnt in grade_cnt:
        for i in range(len(grade)):
            if cnt > grade[i]:
                result[i] += grade_cnt[cnt]
    return result

print(solution([1,1,1,1,1,2]))