# 4874_Forth
# 2022-08-23

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    string = input().split()
    stack = []
    top = -1
    result = 0

    # run time error 방지 위해 다 나눠서 작성
    for s in string:
        if s != '*' and s != '/' and  s != '+' and  s != '-' and s != '.':
            stack.append(int(s))
        elif s == '*':
            if len(stack) < 2: # 스택이 하나만 남았을 때 연산자가 들어오면 오류 출력
                result = 'error'
                break
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
        elif s == '/':
            if len(stack) < 2:
                result = 'error'
                break
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(a//b) # // 무조건 하기
        elif s == '+':
            if len(stack) < 2:
                result = 'error'
                break
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
        elif s == '-':
            if len(stack) < 2:
                result = 'error'
                break
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
        elif s == '.': # len(stack)이 1보다 더 남아있는 경우
            if len(stack) == 1: 
                result = stack[0]
            else:
                result = 'error'

    print('#{} {}'. format(tc, result))