import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
save_list = []
result = [0]*(N-1) + [-1]
