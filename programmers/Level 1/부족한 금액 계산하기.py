def solution(price, money, count):
    cnt = count*(count+1)//2
    if cnt*price < money:
        return 0
    else:
        return cnt*price - money