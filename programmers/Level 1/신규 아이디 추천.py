def solution(new_id):
    answer = ''
    for str in new_id:
        if str.isupper():
            answer += str.lower()
        elif str.alnum() or str in ('-', '_', '.'):
            answer += str

    for str in answer:

    return answer