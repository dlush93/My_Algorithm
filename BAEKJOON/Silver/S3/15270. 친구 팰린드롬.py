def backtracking(num, cnt): # num : 짝지으려는 친구 번호, cnt : 짝지어진 친구 수
    if num == N:                        # 마지막 친구까지 찾으면
        return cnt                      # 짝지어진 친구를 반환
    if couple[num]:                     # 이미 짝지어져 있으면
        return backtracking(num+1, cnt) # 다음 친구로 넘어간다

    res = 0
    for f in friend[num]:   # 현재 친구와 친한친구 리스트
        couple[num] = 1     # 짝 지어질 예정
        if not couple[f]:   # 친한친구가 아직 짝이 지어져있지 않으면
            couple[f] = 1   # 짝지어 준다
            res = max(res, backtracking(num+1, cnt+2)) # 최대로 짝지을 수 있는 값을 구한다.
            couple[f] = 0
        couple[num] = 0
    return max(res, backtracking(num+1, cnt))


N, M = map(int, input().split())
friend = [[] for _ in range(N+1)] # 친구 리스트
couple = [0 for _ in range(N+1)] # 짝지어진 친구 체크
for i in range(M):
    a, b = map(int, input().split())
    friend[min(a, b)].append(max(a,b))
result = backtracking(0, 0)
print(result + 1 if result < N else N) # 짝지어진 결과값이 전체 친구 수보다 작으면 1명 추가