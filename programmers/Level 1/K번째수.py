def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        new_arr = sorted(array[i-1:j])
        answer.append(new_arr[k-1])
    return answer