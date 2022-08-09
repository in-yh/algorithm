# 4831_전기버스
# 2022-08-09

import sys
sys.stdin = open('input.txt', 'r')

def is_possible(K, N, M, charge): # 충전 가능 여부 따로 함수로 정의
    for i in range(M-1):
        if charge[i+1] - charge[i] > K or charge[0] - 0 > K or N - charge[M-1] > K:
            return 0

T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    result = is_possible(K, N, M, charge)

    if result != 0:
        need_charge = []
        j = 0
        while j < N-K:
            for k in range(j+K, j, -1):
                if k in charge:
                    need_charge.append(k)
                    j = k
                    break # break을 쓰면 다시 while로??
                    
        cnt = 0
        for _ in need_charge:
            cnt += 1
        result = cnt
    
    print('#{} {}'. format(t, result))