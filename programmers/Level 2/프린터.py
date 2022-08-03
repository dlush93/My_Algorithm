from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque([idx, p] for idx, p in enumerate(priorities))
    while True:
        now = queue.popleft()
        for q in queue:
            if now[1] < q[1]:
                queue.append(now)
                break
        else:
            answer += 1
            if now[0] == location:
                return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))