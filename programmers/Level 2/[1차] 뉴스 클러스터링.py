from collections import Counter

def solution(str1, str2):
    answer = 0
    s_list1 = [str1[i].lower()+str1[i+1].lower() for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]
    s_list2 = [str2[i].lower()+str2[i+1].lower() for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()]
    if len(s_list1) == 0 and len(s_list2) == 0:
        answer = 1
    else:
        c_list1 = Counter(s_list1)
        c_list2 = Counter(s_list2)
        intersection = c_list1 - (c_list1 - c_list2)
        union = c_list1 + c_list2 - intersection
        union_cnt = 0
        intersection_cnt = 0
        print(union, intersection)
        for u in union.values():
            union_cnt += u
        for i in intersection.values():
            intersection_cnt += i
        answer = intersection_cnt/union_cnt

    return int(answer*65536)

print(solution('FRANCE', 'french'))