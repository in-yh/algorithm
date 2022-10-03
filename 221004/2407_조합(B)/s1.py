# 2407_조합(B)
# 2022-10-03

import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
p = 1
c = 1
for i in range(n, n-m,-1):
    p *= i
for j in range(m, 0, -1):
    c *= j
print(p//c) # // 연산으로

# 깊이가 너무 깊은 듯
# def nCm(N, M, S):
#     global cnt
#     if M == 0:
#         cnt += 1
#         return
#     else:
#         for i in range(S, N-M+1):
#             result[M-1] = a[i]
#             nCm(N, M-1, i+1)

# n, m = map(int, input().split())
# a = [i for i in range(1, n+1)]
# result = [0]*m
# cnt = 0
# nCm(n, m, 0)
# print(cnt)