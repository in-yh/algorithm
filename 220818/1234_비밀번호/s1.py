# 1234_비밀번호
# 2022-08-18

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N, S = input().split()
    N = int(N)
    L = list(S)

    stack = [-1]*N # -1로 설정!!
    top = 0
    stack[top] = L[0]

    for i in range(1, N):
        if L[i] != stack[top]:
            top += 1
            stack[top] = L[i]
        else:
            stack[top] = -1
            top -= 1
    
    result = ''.join(stack[:top+1])
    print('#{} {}'. format(tc, result))