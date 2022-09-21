# 10726_이진수 표현
# 2022-09-20

import sys
sys.stdin = open('input.txt', 'r')

def is_one(n, m):
    i = 0 
    while i < n:
        if m % 2: # m을 2로 나눴을 때, 1이면 m을 //2 해주고 i를 +1 해주기
            m = m // 2
            i += 1
        else: # 0이 나오면 break
            break

    if i == n:
        return 'ON'
    else:
        return 'OFF'


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print('#{} {}'. format(tc, is_one(N, M)))

    
'''
30 / 2 = 15 ... 0
15 / 2 = 7 ... 1
7 / 2 = 3 ... 1
3 / 2 = 1 ... 1
'''