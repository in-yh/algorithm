# 5209_최소 생산 비용
# 2022-09-27

import sys
sys.stdin = open('input.txt', 'r')

def f(row, n, sumc):
    global result
    if row == n: 
        if result > sumc:
            result = sumc
        return

    if result < sumc: # 현재 최소비용보다 커지면 백트래킹
        return 

    for col in range(N):
        if col not in c:
            c.append(col)
            f(row+1, n, sumc+cost[row][col])
            c.pop() # 원상복구
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    result = 100*15*15 # 최초 비교를 위해 최대값 넣어주기
    c = [] # 함수내부에서 col 사용했다면 c에 append
    f(0, N, 0)
    print('#{} {}'.format(tc, result))