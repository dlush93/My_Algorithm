def solution(id_list, report, k):
    answer = []
    id_dict = {i: {'report_cnt': 0, 'report_user': set()} for i in id_list}
    report_set = set(report)
    stop = set()
    for r in report_set:
        x, y = r.split()
        id_dict[x]['report_user'].add(y)
        id_dict[y]['report_cnt'] += 1
        if id_dict[y]['report_cnt'] >= k:
            if y not in stop:
                stop.add(y)
    for value in id_dict.values():
        answer.append(len(value['report_user']&stop))
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))