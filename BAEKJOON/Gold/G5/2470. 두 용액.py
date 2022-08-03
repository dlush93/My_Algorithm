N = int(input())
solution = sorted(list(map(int, input().split())))
alkali, acid, mix = 0, N-1, 999999999999
while alkali < acid:
    if abs(solution[alkali] + solution[acid]) < mix:
        mix = abs(solution[alkali] + solution[acid])
        result = [solution[alkali], solution[acid]]
    if solution[alkali] + solution[acid] < 0:
        alkali += 1
    elif solution[alkali] + solution[acid] > 0:
        acid -= 1
    else:
        print(solution[alkali], solution[acid])
        break
print(*result)