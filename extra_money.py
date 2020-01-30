def coin_count(coin):
    a = [500, 100, 50, 10]
    count = 0
    for i in a:
        if coin%i !=0:
            coin = coin%i
            count += coin//i
        else:
            count += coin//i
    return count

print(coin_count(5760))