# 1859_백만장자 프로젝트
# 2022-08-21

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))

    # 뒤부터 생각하기!!
    earn = 0
    maxIdx = N-1
    for i in range(N-2, -1, -1):
        if L[i] > L[maxIdx]:
            maxIdx = i
        else:
            earn += L[maxIdx] - L[i] 
    
    print('#{} {}'. format(tc, earn))