money = int(input())
coin = 0
if money < 5:
    if money%2:
        print(-1)
    else:
        print(money//2)
else:
    while money >= 0:
        if money%5 == 0:
            coin += money//5
            print(coin)
            break
        else:
            money -= 2
            coin += 1
    else:
        print(-1)