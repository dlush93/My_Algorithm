def solution(s):
    p_cnt = 0
    y_cnt = 0
    for i in s:
        i = i.lower()
        if i == 'p':
            p_cnt += 1
        elif i == 'y':
            y_cnt += 1
    if y_cnt == p_cnt:
        answer = True
    else:
        answer = False
    return answer