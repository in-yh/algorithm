# 1463_1로 만들기(B)
# 2022-10-03

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
DP = [0]*(N+1)
DP[1] = 0
for i in range(2, N+1): # 인덱스 에러 방지 위해 2부터 for문 돌려줘야 함
    DP[i] = DP[i-1]+1 # 3과 2로 나누어 떨어지지 않을 때의 조건을 먼저 만들어줘야 함
    if i%3 == 0:
        DP[i] = min(DP[i//3]+1, DP[i])
    if i%2 == 0:
        DP[i] = min(DP[i//2]+1, DP[i])        

print(DP[N])