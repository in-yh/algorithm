# 4866_괄호검사
# 2022-08-18

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    L = list(input())
    stack = [0]*len(L)
    top = -1
    result = -1 # 정상적으로 짝을 이뤘는지 확인하는 결과값 설정(초기값 : -1)

    for i in range(len(L)):
        if L[i] == '{' or L[i] == '(': # 여는 괄호는 push
            top += 1
            stack[top] = L[i]
        elif L[i] == '}': # 닫는 괄호는 나눠서 고려
            if stack[top] == '{': # stack[top]이 '{'인 경우, pop
                stack[top] = 0
                top -= 1
            else: # stack[top]이 '{'가 아닌 경우, result 0 할당(처음부터 '}' 나오는 거 result 0으로 처리, stack 비어있어서 아래 if문에서 처리 못함)과 함께 break
                result = 0
                break
        elif L[i] == ')':
            if stack[top] == '(': 
                stack[top] = 0
                top -= 1
            else:
                result = 0
                break
    
    # stack이 비어있으면 정상적으로 짝을 이룬 경우로 result 1 할당
    if top == -1 and result != 0:
        result = 1
    else: # '('이 하나 남는 경우처럼 위에서 걸러내지 못한 경우가 있으므로 넣어줘야 함
        result = 0
    
    print('#{} {}'. format(tc, result))