N = int(input())
mountain = list(map(int, input().split()))
kill = 0
for i in range(N):
    cnt = 0
    for j in range(i+1, N):
        if mountain[i] > mountain[j]:
            cnt +=1
        else:
            break
    kill = max(cnt, kill)
    if N-i < kill:
        break
print(kill)