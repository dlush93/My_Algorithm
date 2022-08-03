def break_chk(egg1, egg2):
    if egg1[0] <= egg2[1] and egg2[0] <= egg1[1]:
        return 2
    elif egg2[0] <= egg1[1] :
        return 1
    else:
        return 0

def backtracking(egg, cur):
    global max_cnt
    if cur == N:
        max_cnt = max()

    if broken[cur]:
        for i in range(N):
            if i == cur or broken[i] == 0:
                continue
            if broken[i]:
                if break_chk(egg[cur], egg[i]) == 2:
                    broken[cur], broken[i] = 0, 0
                    backtracking(cur + 1)
                elif break_chk(egg[cur], egg[i]) == 1:
                    pass
                else:
                    pass

    else:
        backtracking(cur+1)


N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
broken = [1 for _ in range(N)]
max_cnt = 0
