lang = {'python':0, 'java':1, 'cpp':2}
position = {'backend':0, 'frontend':1}
career = {'junior':0, 'senior':1}
food = {'chicken':0, 'pizza':1}

def solution(info, query):
    data = [list(info[i].split()) for i in range(len(info))]
    orders = [list(query[i].split(' and ')) for i in range(len(query))]
    for i in orders:
        i.extend(i.pop().split())
    result = []
    for order in orders:
        index = set(range(len(info)))
        idx = 0
        for o in order:
            if o == '-':
                idx += 1
                continue
            for i in list(index):
                if o.isdigit():
                    if int(o) > int(data[i][-1]):
                        index.discard(i)
                elif o != data[i][idx]:
                    index.discard(i)
            idx += 1
        result.append(len(index))
    return result

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))