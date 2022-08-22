# 연습문제1_후위표기법
# 2022-08-22

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = [0] * len(string)
    top = -1

    result = ''
    for s in string:
        if s == '+' or s == '-' or s == '/' or s == '*':
            top += 1
            stack[top] = s
        else:
            result += s

    while top > -1: # -1 초과로 하기!! -1 포함하면 stack[-1] 즉, 0까지 출력됨..
        result += stack[top]
        top -= 1

    print('#{} {}'. format(tc, result))