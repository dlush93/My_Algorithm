def solution(n):
    answer = 0
    ternary = ''
    while n:
        temp = n%3
        ternary += str(temp)
        n //= 3
    for i in range(len(ternary)):
        answer += 3**(len(ternary)-1-i)*int(ternary[i])
    return answer

print(solution(125))