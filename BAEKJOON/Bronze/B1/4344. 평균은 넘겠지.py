for t in range(int(input())):
    data = list(map(int, input().split()))
    student = data[0]
    average = sum(data[1:])/student
    cnt = 0
    for i in range(1, student+1):
        if data[i] > average:
            cnt += 1
    result = round(cnt/student*100, 3)
    print("{0:.3f}%".format(result))