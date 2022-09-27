# 5208_전기버스2
# 2022-09-27

import sys
sys.stdin = open('input.txt', 'r')

# 충전을 하고 갈 수 있는 곳에서 가장 큰 충전을 채택(반복) <백트래킹 이용>
def charge(i, cnt):
    global result
    
    if i + stop[i] >= N:
        result = cnt
        return

    if cnt >= result:
        return
    
    for j in range(i+1, i+stop[i]+1):
        charge(j, cnt+1)
    

T = int(input())
for tc in range(1, T+1):
    M = list(map(int, input().split()))
    N = M.pop(0)

    stop = [0]*(N+1) # 정류장을 인덱스로 충전지 개수 리스트
    for i in range(1, N):
        stop[i] = M[i-1]
    
    result = 101
    charge(1, 0) # 1번 정류장, 0번 충전

    print('#{} {}'.format(tc, result))