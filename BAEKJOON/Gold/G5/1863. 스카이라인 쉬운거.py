import sys
input = sys.stdin.readline

n = int(input())
skyline = []
width = height = 0
for _ in range(n):
    w, h = map(int, input().split())
    width = max(w, width)
    height = max(h, height)
    skyline.append([w, h])
building_hieght = 1
while building_hieght <= height:
