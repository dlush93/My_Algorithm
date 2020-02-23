for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    grade = ['A+']*(N//10) + ['A0']*(N//10) + ['A-']*(N//10) + ['B+']*(N//10) + ['B0']*(N//10) + ['B-']*(N//10) + ['C+']*(N//10) + ['C0']*(N//10) + ['C-']*(N//10) + ['D0']*(N//10)
    score = []
    for n in range(N):
        data = list(map(int, input().split()))
        score.append(data[0]*35 + data[1]*45 + data[2]*20)
    student = score[K-1]
    score.sort(reverse = True)
    rank = 0
    for r,s in enumerate(score):
        if s == student:
            rank = r
            break
    print('#{} {}'.format(t, grade[rank]))