def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            answer += chr(65 + (ord(i)-65+n)%26)
        elif i.islower():
            answer += chr(97 + (ord(i)-97+n)%26)
        else:
            answer += ' '
    return answer