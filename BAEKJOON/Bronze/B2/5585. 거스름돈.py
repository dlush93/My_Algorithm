money = int(input())
coin = 1000 - money
cnt = 0
while coin != 0:
    if coin >= 500:
        coin -= 500
        cnt += 1
    elif coin >= 100:
        coin -= 100
        cnt += 1
    elif coin >= 50:
        coin -= 50
        cnt += 1
    elif coin >= 10:
        coin -= 10
        cnt += 1
    elif coin >= 5:
        coin -= 5
        cnt += 1
    else:
        coin -= 1
        cnt +=1
print(cnt)
