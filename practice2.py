test = int(input())
for t in range(1,test+1):
    N = int(input())
    ai = [int(x) for x in input()]
    numbers = {}
    for i in ai:
        numbers[i] = ai.count(i)
    result_num = 0
    result_cnt = 0
    for num, cnt in numbers.items():
        if



