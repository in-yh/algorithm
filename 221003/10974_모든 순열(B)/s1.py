# 10974_모든 순열(B)
# 2022-10-03

import sys
sys.stdin = open('input.txt', 'r')

def f(i, k):
    if i == k:
        print(*p)
    else:
        for j in range(k):
            if used[j] == 0: # a[j]가 아직 사용되지 않았으면
                used[j] = 1 # a[j] 사용됨으로 표시
                p[i] = a[j] # p[i]는 a[j]로 결정
                f(i+1, k) # p[i+1] 값을 결정하러 이동
                used[j] = 0 # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = int(input())
a = [i for i in range(1, N+1)]
used = [0]*N
p = [0]*N
f(0, N)

# def f(i, N): # 순서대로 출력이 되진 않음
#     if i == N:
#         print(P)
#     for j in range(i, N):
#         P[i], P[j] = P[j], P[i]
#         f(i+1, N)
#         P[i], P[j] = P[j], P[i]

# N = int(input())
# P = [i for i in range(1, N+1)]
# f(0, N)