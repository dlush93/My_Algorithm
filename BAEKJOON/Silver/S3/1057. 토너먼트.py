N, num1, num2 = map(int, input().split())
cnt = 0
num = 2
now_round = 1
while True:
    if (now_round-1)*num < num1 <= now_round*num and (now_round-1)*num < num2 <= now_round*num:
        print(now_round)
        break
