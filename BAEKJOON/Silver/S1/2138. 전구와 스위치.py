def first_push():
    now_state = now[:]
    now_state[0] = (now_state[0]+1)%2
    now_state[1] = (now_state[1]+1)%2
    cnt = 1
    for i in range(1, N):
        if now_state == target:
            return cnt
        if i == N-1:
            if now_state[i-1] != target[i-1]:
                now_state[i-1] = not now_state[i-1]
                now_state[i] = not now_state[i]
                cnt += 1
        else:
            if now_state[i-1] != target[i-1]:
                now_state[i-1] = not now_state[i-1]
                now_state[i] = not now_state[i]
                now_state[i+1] = not now_state[i+1]
                cnt += 1
    if now_state == target:
        return cnt
    return -1


def first_no_push():
    now_state = now[:]
    cnt = 0
    for i in range(1, N):
        if now_state == target:
            return cnt
        if i == N-1:
            if now_state[i-1] != target[i-1]:
                now_state[i-1] = not now_state[i-1]
                now_state[i] = not now_state[i]
                cnt += 1
        else:
            if now_state[i-1] != target[i-1]:
                now_state[i-1] = not now_state[i-1]
                now_state[i] = not now_state[i]
                now_state[i+1] = not now_state[i+1]
                cnt += 1
    if now_state == target:
        return cnt
    return -1


N = int(input())
now = list(map(int, input()))
target = list(map(int, input()))
result1, result2 = first_push(), first_no_push()
if result1 + result2 == -2:
    print(-1)
else:
    print(max(result1, result2))