def solution(n):
    answer = 0
    temp = []
    div = divmod(n, 3)
    temp.append(div[1])
    while div[0] != 0:
        div = divmod(div[0], 3)
        temp.append(div[1])
    print(temp)
    return str(answer)

print(solution(3))