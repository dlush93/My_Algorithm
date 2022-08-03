from math import ceil

def solution(fees, records):
    answer = []
    cost = dict()
    end_minute = 23*60 + 59
    for record in records[::-1]:
        time, num, hist = record.split()
        minute = int(time[:2])*60 + int(time[3:])
        if num not in cost:
            cost[num] = [-1, 0]
        if hist == 'IN':
            if cost[num][0] == -1:
                cost[num][1] += end_minute - minute
            else:
                cost[num][1] += cost[num][0] - minute
        else:
            cost[num][0] = minute

    sorted_num = sorted(cost)
    for num in sorted_num:
        if cost[num][1] - fees[0] > 0:
            answer.append(fees[1] + ceil((cost[num][1] - fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))