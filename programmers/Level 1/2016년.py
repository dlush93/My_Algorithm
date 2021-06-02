def solution(a, b):
    day = {1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6:"WED", 0:"THU"}
    month = {1:0, 2:31, 3:60, 4:91, 5:121, 6:152, 7:182, 8:213, 9:244, 10:274, 11:304, 12:335}
    answer = day[(month[a]+b)%7]
    return answer
print(solution(5, 24))