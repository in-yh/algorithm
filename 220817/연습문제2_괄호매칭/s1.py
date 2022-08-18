# 연습문제2_괄호매칭
# 2022-08-17

import sys
sys.stdin = open('input.txt', 'r')

def length(x):
    cnt = 0
    for _ in x:
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    s = input() # ))))
    stack = [0] * length(s) # 공백스택 [0, 0, 0,...]
    top = -1 
    result = 0 # 괄호매칭 결과 출력할 값

    for i in range(length(s)):
        if s[i] == '(': # '('이면 top 증가시키고, stack[top]에 '(' 넣어주기
            top += 1
            stack[top] = '('
        elif s[i] == ')': # ')'이면 두 가지로 나뉨
            if stack[top] == '(': # 앞에 '('가 있으면 stack[top]을 꺼내고(0으로 바꾸고) top 감소
                stack[top] = 0 
                top -= 1
            else: # 앞에 '('가 없으면 오류
                result = -1
                break
        
    if stack == [0] * length(s) and result != -1: # 스택이 비어있거나, 위에서 result가 -1이 아닌 경우
        result = 1
    else:
        result = -1

    print('#{} {}'. format(tc, result))