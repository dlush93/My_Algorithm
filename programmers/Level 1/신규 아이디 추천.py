def solution(new_id):
    answer = ''
    cnt = 0
    for i in new_id:
        if cnt == 1 and i != '.':
            answer += '.'
            cnt = 0
        if i.isupper():
            answer += i.lower()
        elif i.isalnum():
            answer += i
        elif i == '-' or i == '_':
            answer += i
        elif i == '.':
            cnt = 1
        elif i == ' ':
            answer += 'a'
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) == 0:
        answer = 'aaa'
    if answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
    return answer