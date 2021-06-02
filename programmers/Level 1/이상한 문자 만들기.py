def solution(s):
    answer = ''
    cnt = 0
    for i in s:
        if i.isalpha():
            if cnt%2:
                answer += i.lower()
                cnt += 1
            else:
                answer += i.upper()
                cnt += 1
        else:
            answer += ' '
            cnt = 0
    return answer
solution("try hello world")