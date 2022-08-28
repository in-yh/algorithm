# 1224_계산기3
# 2022-08-28

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    string = input()
    stack = [0] * N
    top = -1

    icp = {'(':3, '*':2, '+':1}
    isp = {'(':0, '*':2, '+':1}
    
    ## 후위표기하기

    # 숫자가 들어오면 출력
    # 연산자가 들어올 때(닫는괄호 제외한) 
        # top에 연산자가 없으면 push!!
        # icp가 isp보다 크다면 push
        # icp가 isp보다 작거나 같다면 낮은 isp가 보일 때까지 pop하고 출력한 후 그 다음에 push 
    # 닫는괄호가 나오면 여는괄호 나올 때까지 pop하여 출력!!(여는괄호는 버림)
    # string 순회 끝나면 스택에 남은 거 다 출력

    result = ''
    for s in string:
        if s != '(' and s != '*' and s != '+' and s != ')':
            result += s
        elif s == '(' or s == '*' or s == '+':
            if top == -1 or icp[s] > isp[stack[top]]:
                top += 1
                stack[top] = s
            else: # 들어오는게 작거나 같은 경우
                if top == -1: # 비어있으면 (비어있는 경우를 나눠서 하는게 맞는 것 같음!!)
                    break
                else: # 안 비어있으면 
                    while icp[s] <= isp[stack[top]]:
                        result += stack[top]
                        top -= 1
                top += 1
                stack[top] = s
        elif s == ')':
            while stack[top] != '(':
                result += stack[top]
                top -= 1
            top -= 1
    
    while top > -1:
        result += stack[top]
        top -= 1

    ## 계산하기
    stack = [0] * N
    top = -1
    for r in result:
        if r != '*' and r != '+': # 숫자라면 push
            top += 1
            stack[top] = r
        elif r == '+': # 연산자라면 stack 안 2개 pop한 후 계산하여 결과값 다시 push 
            answer = int(stack[top-1]) + int(stack[top])
            top -= 1
            stack[top] = answer
        elif r == '*': 
            answer = int(stack[top-1]) * int(stack[top])
            top -= 1
            stack[top] = answer
        
    print('#{} {}'. format(tc, stack[top]))