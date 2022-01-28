from collections import deque

def dfs():                                      # 8. dfs(depth-first search) 깊이 우선 탐색 함수를 정의한다.
                                                #    https://ko.wikipedia.org/wiki/%EA%B9%8A%EC%9D%B4_%EC%9A%B0%EC%84%A0_%ED%83%90%EC%83%89
    stack = []                                  # 9. 감염된 컴퓨터를 저장하기 위한 리스트
    stack.append(1)                             # 10. 감염되어있는 1번 컴퓨터를 리스트에 저장
    cnt = 0                                     # 11. 1번 컴퓨터를 통해 감염된 컴퓨터의 수를 저장하기 위한 변수
    while stack:                                # 12. 더이상 감염된 컴퓨터가 없을 때까지 while 문을 반복
        virus = stack.pop()                     # 13. 바이러스에 감염된 컴퓨터를 stack에서 꺼냄
        for i in graph[virus]:                  # 14. 바이러스가 감염된 컴퓨터와 연결되어 있는 컴퓨터가 연결된 컴퓨터를 for 문으로 반복
            if visited[i]:                      # 15. 만약 이미 이 컴퓨터가 감염이 되어있지 않다면?
                cnt += 1                        #     감염된 컴퓨터의 수를 1대 증가
                visited[i] = 0                  #     이 컴퓨터가 감염된 컴퓨터라고 체크
                stack.append(i)                 #     감염된 컴퓨터는 stack 리스트에 저장

    return cnt                                  # 16. 더이상 감염시킬 컴퓨터가 없으면 while 문이 종료되고 감염된 컴퓨터의 수를 return

#
# def bfs():
#     q = deque()
#     q.append(1)
#     cnt = 0
#     while q:
#         virus = q.popleft()
#         for i in graph[virus]:
#             if visited[i]:
#                 cnt += 1
#                 visited[i] = 0
#                 q.append(i)
#
#     return cnt


computer = int(input())                         # 1. 컴퓨터의 수
network = int(input())                          # 2. 컴퓨터와 연결된 네트워크 쌍의 수
graph = [[] for _ in range(computer+1)]         # 3. 컴퓨터끼리 연결되어있는지 확인하기 위한 리스트
visited = [1 for _ in range(computer+1)]        # 4. 컴퓨터가 감염되었는지 확인하기 위한 리스트 0은 감염, 1은 감염되지 않음
visited[1] = 0                                  # 5. 1번 컴퓨터가 바이러스에 걸려있기 때문에 감염된 것으로 체크
for _ in range(network):                        # 6. 네트워크 쌍의 수 만큼 for 문을 반복
    com1, com2 = map(int, input().split())      # 7. 네트워크 쌍은 서로 연결되어 있으므로 graph에 값을 둘 다 넣어준다.
    graph[com1].append(com2)                    # ex) 1 2가 들어오면 graph의 1번 인덱스 즉 1번 컴퓨터와 2번 컴퓨터가
    graph[com2].append(com1)                    #     연결되어 있다는 것을 나타내기 위해 graph[1]에 2를 넣어주고
                                                #     graph[2]에도 1을 넣어준다.
print(dfs())                                    # 17. 감염된 컴퓨터의 수 출력