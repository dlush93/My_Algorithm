N = int(input())                            # 도시의 갯수
road = list(map(int, input().split()))      # 인접한 도시를 연결하는 도로의 길이
cost = list(map(int, input().split()))      # 도시별 기름 값
now_cost = 1000000000                       # 지나는 도시의 기름값과 비교하여 더 저렴한 가격을 저장
whole_cost = 0                              # 비용을 저장하는 변수
for i in range(N-1):                        # 첫 도시부터 마지막 도시까지 가는데 마지막 도시의 기름 값은 필요없으므로 N-1 까지 반복
    if cost[i] < now_cost:                  # 현재 도시의 기름값과 저장된 기름값과 비교하여
        now_cost = cost[i]                  # 더 저렴한 기름값을 저장
    whole_cost += now_cost*road[i]          # 저장된 기름값과 거리를 곱하여 전체비용을 저장하는 변수에 저장
print(whole_cost)