def find(num, cnt):

    global min_num

    if num >= min_num:
        return
    if cnt == V:
        min_num = num
        print(cnt, num)
        return

    for i in range(V):
        for j in range(V):
            if count[j] != 0 and graph[i][j] != 0:
                count[j] -= 1
                print(cnt, num, count, visit)
                find(num + graph[i][j], cnt + 1)
                count[j] += 1


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for i in range(V+1)]
    visit = [0]*(V+1)
    count = [0]*(V+1)
    for i in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w
        count[n1] += 1
    min_num = 10000000
    find(0, 0)
    print(min_num)
