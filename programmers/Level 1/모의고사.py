def solution(answers):
    answer = []
    mg1 = [1, 2, 3, 4, 5]
    mg2 = [2, 1, 2, 3, 2, 4, 2, 5]
    mg3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0]*3
    for i in range(len(answers)):
        if answers[i] == mg1[i%5]:
            cnt[0] += 1
        if answers[i] == mg2[i%8]:
            cnt[1] += 1
        if answers[i] == mg3[i%10]:
            cnt[2] += 1
    for i in range(3):
        if max(cnt) == cnt[i]:
            answer.append(i+1)
    return answer