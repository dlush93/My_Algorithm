N = int(input())
shop = list(map(int, input().split()))
milk = 0
cnt = 0
for i in shop:
    if i == milk:
        milk += 1
        milk = milk%3
        cnt += 1
print(cnt)