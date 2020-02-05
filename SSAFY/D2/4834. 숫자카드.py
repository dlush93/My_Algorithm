test = int(input())
for t in range(1,test+1):
    N = int(input())
    ai = ' '.join(input())
    num = list(map(int, ai.split()))
    result = [0]*10
    for i in range(N):
        result[num[i]] +=1
    max_num = 0
    max_idx = 0
    for idx, value  in enumerate(result):
        if value >= max_num:
            max_num = value
            max_idx = idx
    print(f'#{t} {max_idx} {max_num}')