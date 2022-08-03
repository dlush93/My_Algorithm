from itertools import combinations


def solution(orders, course):
    answer = []
    course_dict = {}

    for c in course:
        if c not in course_dict:
            course_dict[c] = {}
        for o in orders:
            for comb in combinations(sorted(list(o)), c):
                if comb not in course_dict[c]:
                    course_dict[c][comb] = 0
                course_dict[c][comb] += 1
    for c in course:
        result = [k for k, v in course_dict[c].items() if max(course_dict[c].values()) == v and v > 1]
        for r in result:
            answer.append(''.join(r))
    return sorted(answer)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]	))