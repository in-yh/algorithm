# 2170_선 긋기(B)
# 2022-08-22

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
L = [0] * 2000000001 # -1000000000 <= x < y <= 1000000000
A = 1000000000
B = -1000000000
for i in range(N):
    a, b = map(int, input().split())
    L[1000000000+a:1000000000+b] = [1] * (b-a)
    
    # a의 최소값, b의 최대값 구하기
    if A > a:
        A = a
    if B < b:
        B = b

result = L.count(1)
print(result)