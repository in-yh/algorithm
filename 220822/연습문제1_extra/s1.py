# 연습문제1_extra
# 2022-08-22

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = [0] * len(string)
    top = -1

    isp = {'*':2, '/':2, '+':1, '-':1, '(':0}
    icp = {'*':2, '/':2, '+':1, '-':1, '(':3}

    result = ''
    for s in string:
        if s != '*' and s != '/' and s != '+' and s != '-' and s != '(' and s != ')': # 피연산자면 출력
            result += s
        elif s == '*' or s == '/' or s == '+' or s == '-' or s == '(': # 연산자라면
            if top == -1 or isp[stack[top]] < icp[s]: # 1.스택이 비어있거나 2.스택 top 연산자<들어가는 연산자라면, push
                top += 1
                stack[top] = s
            else:
                while isp[stack[top]] >= icp[s]: # 스택 top에 있는 연산자의 우선순위가 낮아질 때까지 pop한 후 push
                    if top == 0: # top이 0이라면 pop하고 바로 break
                        result += stack[top]
                        top -= 1
                        break
                    else:
                        result += stack[top]
                        top -= 1
                top += 1
                stack[top] = s
        elif s == ')': # 오른쪽 괄호이면 왼쪽 괄호 나올 때까지 pop한 후 출력, 왼쪽괄호 만나면 pop하고 출력은 안 한다.
            while stack[top] != '(':
                result += stack[top]
                top -= 1
            top -= 1
        
    while top > -1: # stack에 남은 연산자들 모두 pop하여 출력
        result += stack[top]
        top -= 1
    
    print('#{} {}'. format(tc, result))