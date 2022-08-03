def solution(s):
    s_list = list(s)
    temp = []
    for i in range(len(s_list)):
        if len(temp) == 0:
            temp.append(s_list[i])
        elif s_list[i] == temp[-1]:
            temp.pop()
        else:
            temp.append(s_list[i])

    if len(temp) == 0:
        return 1
    else:
        return 0

print(solution('baabaa'))
print(solution('cdcd'))