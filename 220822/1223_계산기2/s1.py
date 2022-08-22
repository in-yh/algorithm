# 1223_계산기2
# 2022-08-22

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    string = input()
    stack = [0] * N
    top = -1

    # 후위표기법으로 변환
    isp = {'*':2, '+':1}
    icp = {'*':2, '+':1}

    result = ''
    for s in string:
        if s != '+' and s != '*': # 피연산자면 출력
            result += s
        elif s == '+' or s == '*': # 연산자라면
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
        
    while top > -1: # stack에 남은 연산자들 모두 pop하여 출력
        result += stack[top]
        top -= 1

    # 계산하기
    for s in result: # 첫 번째 결과값을 for문 돌리기
        if s != '+' and s != '*': # 피연산자면 push
            top += 1
            stack[top] = s
        elif s == '+' or s == '*': # 연산자면 두개 pop하여 연산 수행 후 결과값 push
            b = stack[top]
            top -= 1
            a = stack[top]
            top -= 1
            if s == '+':
                c = int(a) + int(b)
            elif s == '*':
                c = int(a) * int(b)
            top += 1
            stack[top] = c
            
    result2 = stack[top]
    print('#{} {}'. format(tc, result2))