# 4873_반복문자 지우기
# 2022-08-18

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    L = list(input()) # ['A', 'B', 'C', 'C', 'B']
    top = 0 # stack 첫 값에 L[0] 미리 넣어두기
    stack = [0]*len(L) # 미리 초기화
    stack[top] = L[0] 

    # L 순회하며 stack[top] 값이랑 같으면 pop하고, 다르면 push한다.
    for i in range(1, len(L)):
        if L[i] == stack[top]:
            stack[top] = 0 # ==이 아니라 =
            top -= 1  
        else:
            top += 1
            stack[top] = L[i]

    # stack에서 0이 아닌 문자 숫자 구하기
    cnt = 0
    for s in stack:
        if s != 0:
            cnt += 1

    print('#{} {}'. format(tc, cnt))