for t in range(1, int(input())+1):
    day, month1, month3, year = map(int, input().split())
    data = list(map(int, input().split()))
    min_price = min(sum(data)*day, year)
    month = 0
    for i in data:
        month +=1