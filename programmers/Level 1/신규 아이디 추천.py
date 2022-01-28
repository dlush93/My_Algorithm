def solution(new_id):
    answer = ''
    # 1. 대문자 처리 및 특수문자 처리
    for i in new_id:
        if i.isalnum():
            answer += i.lower()
        elif i in ('-', '_', '.'):
            answer += i
    # 2. 중복 특수문자 처리 및 앞 뒤자리 . 제거

    cnt = 0
    temp = ''
    for i in answer:
        if i == '.':
            cnt = 1
        elif cnt == 1:
            cnt = 0
            temp += '.' + i
        else:
            temp += i
    else:
        answer = temp

    answer = answer.rstrip('.')
    answer = answer.lstrip('.')

    # 3. 글자수 정리

    if len(answer) == 0:
        answer = 'aaa'
    elif len(answer) < 3:
        answer = answer + answer[-1] * (3- len(answer))
    if len(answer) > 15:
        answer = answer[:15]
    answer = answer.rstrip('.')

    return answer

print(solution("123_.def"))