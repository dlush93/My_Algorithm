def solution(s):
    answer = ''
    temp = ''
    converter = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
                 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for n in s:
        if not n.isdigit():
            temp += n
            if temp in converter:
                answer += converter[temp]
                temp = ''
        else:
            answer += n
    else:
        if temp:
            answer += converter[temp]
    return answer