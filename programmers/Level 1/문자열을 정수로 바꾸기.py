def solution(s):
    answer = 0
    sign = {'-':-1, '+':1}
    if s[0].isdigit():
        answer = int(s)
    else:
        answer = sign[s[0]]*int(s[1:])
    return answer