# 2170_선 긋기(B)
# 2022-08-23

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
L = []
for i in range(N):
    a, b = map(int, input().split())
    L.append((a, b))
L.sort() # 시작점 기준 정렬(무조건 앞에 있는 튜플의 시작점이 앞에 있다.)

result = L[0][1] - L[0][0]
for j in range(3):
    # 뒤 튜플 시작점과 종착점이 모두 앞 튜플 종착점보다 작은 경우
    if L[j][1] >= L[j+1][0] and L[j][1] >= L[j+1][1]:
        pass
    # 뒤 튜플 시작점과 종착점 사이에 앞 튜플 종착점이 있는 경우
    elif L[j+1][0] < L[j][1] < L[j+1][1]:
        result += L[j+1][1] - L[j][1]
    # 앞 튜플 종착점 이후에 뒤 튜플 시작점이 나오는 경우
    elif L[j][1] < L[j+1][0]:
        result += L[j+1][1] - L[j+1][0]

print(result)