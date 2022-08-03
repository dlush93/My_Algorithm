def solution(s):
    temp = [set(map(int, t.split(','))) for t in s[2:-2].split('},{')]
    temp.sort(key=lambda x: len(x))
    answer = list(temp[0])
    for i in range(1, len(temp)):
        answer.append((temp[i]-temp[i-1]).pop())
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))