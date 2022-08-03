# import sys
# input = sys.stdin.readline
#
# def backtracking(arr):
#     global min_diff
#
#     if len(arr) > 1 and arr[-2] > arr[-1]:
#         return
#     if tuple(arr) in comb:
#         return
#
#     if len(arr) == N//2:
#         start = []
#         link = []
#         for i in range(N):
#             if i in arr:
#                 start.append(i)
#             else:
#                 link.append(i)
#         comb.add(tuple(start))
#         comb.add(tuple(link))
#         diff = 0
#         for i in range(N//2):
#             for j in range(N//2):
#                 diff += status[start[i]][start[j]]
#                 diff -= status[link[i]][link[j]]
#         min_diff = min(min_diff, abs(diff))
#         return
#
#     for i in range(N):
#         if i not in arr:
#             arr.append(i)
#             backtracking(arr)
#             arr.pop()
#
#
# N = int(input())
# status = [list(map(int, input().split())) for _ in range(N)]
# comb = set()
# min_diff = 10000000000000
# backtracking([])
# print(min_diff)

