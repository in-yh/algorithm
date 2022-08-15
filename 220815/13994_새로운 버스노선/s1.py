# 13994_새로운 버스노선
# 2022-08-15

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [0]*1001 # 하나 더 추가해서 아래 인덱스 헷갈리는 것 방지하기
    for n in range(N):
        k, s, e = map(int, input().split())
        L[s] += 1 # 시작점 미리 +1
        L[e] += 1 # 종착점 미리 +1
        if k == 1: # 일반버스
            for i in range(s+1, e):
                L[i] += 1

        elif k == 2: # 급행버스
            if s%2 == 0:
                for j in range(s+1, e):
                    if j%2 == 0:
                        L[j] += 1
            else:
                for l in range(s+1, e):
                    if l%2 == 1:
                        L[l] += 1

        elif k == 3: # 광역급행버스
            if s%2 == 0:
                for m in range(s+1, e):
                    if m%4 == 0:
                        L[m] += 1
            else:
                for n in range(s+1, e):
                    if n%3 == 0 and n%10 != 0:
                        L[n] += 1

    maxV = 0 
    for a in range(1001): # maxV 값을 최대 3으로 한정한게 폐인.. 노선 N이 1이상 100이하이므로 100도 나올 수 있음..
        if L[a] > maxV:
            maxV = L[a] 

    print('#{} {}'. format(tc, maxV))