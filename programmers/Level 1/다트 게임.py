def solution(dartResult):
    point = ''
    game = [0]*3
    cnt = 0
    for d in dartResult:
        if d.isdigit():
            point += d
        elif d == 'S':
            game[cnt] = int(point)
            point = ''
            cnt += 1
        elif d == 'D':
            game[cnt] = int(point)**2
            point = ''
            cnt += 1
        elif d == 'T':
            game[cnt] = int(point)**3
            point = ''
            cnt += 1
        elif d == '*':
            if cnt == 1:
                game[cnt-1] *= 2
            else:
                game[cnt-1] *= 2
                game[cnt-2] *= 2
        elif d == '#':
            game[cnt-1] *= -1
    answer = sum(game)
    return answer
solution('1S2D*3T')