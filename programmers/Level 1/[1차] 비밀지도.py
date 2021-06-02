def solution(n, arr1, arr2):
    answer = ['' for _ in range(n) ]
    map1 = ['0'*(n - len(bin(i)[2:])) + bin(i)[2:] for i in arr1]
    map2 = ['0'*(n - len(bin(i)[2:])) + bin(i)[2:] for i in arr2]
    for i in range(n):
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                answer[i] += '#'
            else:
                answer[i] += ' '
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))