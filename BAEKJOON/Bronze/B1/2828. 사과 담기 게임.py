N, M = map(int, input().split())
J = int(input())
basket = []
cnt = 0
for i in range(1, M+1):
    basket.append(i)
for i in range(J):
    apple = int(input())
    move = 0
    if apple > basket[-1]:
        move = apple - basket[-1]
        cnt += move
        for j in range(M):
            basket[j] = basket[j] + move
    elif apple < basket [0]:
        move = basket[0] - apple
        cnt += move
        for k in range(M):
            basket[k] = basket[k] - move
print(cnt)
