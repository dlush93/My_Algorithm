def min_find(w, h):
    for i in range(2, min(w, h)+1):
        while w%i == 0 and h%i == 0:
            w //= i
            h //= i
    return [w, h]

def solution(w,h):
    min_size = min_find(w, h)
    answer = w*h - (max(min_size) + min(min_size) - 1)*(w//min_size[0])
    return answer

print(solution(8, 8))