from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.reverse()
    cross_bridge = deque()
    cross_bridge.append(truck_weights.pop())
    while truck_weights:
        for i in range(len(truck_weights)):
            if truck_weights and sum(cross_bridge) + truck_weights[-1] <= weight:
                cross_bridge.append(truck_weights.pop())
                answer += 1
        for i in range(len(cross_bridge) - bridge_length):
            cross_bridge.popleft()

        while cross_bridge:
            cross_bridge.popleft()

    return answer

print(solution(2, 10, [7,4,5,6]))