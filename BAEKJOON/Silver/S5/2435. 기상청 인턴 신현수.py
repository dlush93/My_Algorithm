N, K = map(int, input().split())
temperature = list(map(int, input().split()))
print(max([sum(temperature[i:i+K]) for i in range(N-K+1)]))