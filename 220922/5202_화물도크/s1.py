# 5202_화물도크
# 2022-09-22

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = []
    for _ in range(N):
        s, e = map(int, input().split())
        time.append((s, e))

    # sort해주고
    # 이전 끝나는 시간보다 다음 시작하는 시간이 크거나 같으면, 결과값+1 해주고 다음으로 채택
    time.sort(key = lambda x: x[1]) # x[1] 기준으로 정렬됨 / lambda x: 를 빼면 x가 정의되어 있지 않다고 에러남
    i = 0
    result = 1 # 1로 해줘야 함(while 들어갈 때 첫 스케쥴은 자동 채택)
    while i < N-1:
        for j in range(i+1, N):
            if time[i][1] <= time[j][0]:
                result += 1
                i = j
                break
        else:
            i = N-1   

    print('#{} {}'.format(tc, result))