from math import factorial

N, K = map(int, input().split())
# result = 1
# if K == 0:
#     print(int(result))
# else:
#     for n in range(1, N+1):
#         result *= n
#     for k in range(1, K+1):
#         result /= k
#     for i in range(1, N-K+1):
#         result /= i
#     print(int(result))

print(factorial(N)//(factorial(K)*factorial(N-K)))