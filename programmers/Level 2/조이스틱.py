def solution(name):
    answer = 0
    min_left_right = len(name)-1
    for idx, n in enumerate(name):
        answer += min(abs(ord('A') - ord(n)), 26-abs(ord('A')-ord(n)))
        next_idx = idx+1
        while next_idx < len(name):
            if name[next_idx] != 'A':
                break
            next_idx += 1
        min_left_right = min(min_left_right, idx*2+len(name)-next_idx, (len(name)-next_idx)*2+idx)
    answer += min_left_right
    return answer

'''
0123456
JAN
'''

print(solution('JAN'))
print(solution('JEROEN'))