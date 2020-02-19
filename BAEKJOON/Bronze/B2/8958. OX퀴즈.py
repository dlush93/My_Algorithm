for t in range(int(input())):
    data = list(input())
    score = 0
    combo = 0
    for i in range(len(data)):
        if data[i] =='O':
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)