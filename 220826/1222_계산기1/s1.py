# 1222_계산기1
# 2022-08-26

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    length = int(input())
    calculate = input()

    # 후위표기법으로 변환
    # 1. 피연산자면 출력
    # 2. 넣는 연산자 우선순위가 스택 top에 있는 연산자 우선순위보다 높으면 push하고 그렇지 않으면 낮은 우선순위가 나올 때까지 pop & 출력 후 push
    #    (연산자면 비어있으면 스택에 넣기) 
    # 3. 남은 연산자 있으면 출력

    stack = [0]*length
    top = -1
    result = ''
    for i in range(length):
        if calculate[i] != '+':
            result += calculate[i]
        else:
            if top == -1:
                top += 1
                stack[top] = calculate[i]
            else:
                result += stack[top]
                stack[top] = calculate[i]
    
    while top != -1:
        result += stack[top]
        top -= 1

    # 계산하기
    # 1. 피연산자면 push
    # 2. 연산자면 2개 pop한 후, 계산한 결과값 push
    # 3. 계산 끝나면 스택에 남아있는 하나의 값 pop & 출력

    stack2 = [0]*length
    top2 = -1
    for j in range(length):
        if result[j] != '+':
            top2 += 1
            stack2[top2] = result[j]
        else:
            a = int(stack2[top2-1]) + int(stack2[top2]) # 문자열이기에 int로 바꿔줌
            top2 -= 1
            stack2[top2] = a
            
    while top2 != -1:
        answer = stack2[top2]
        top2 -= 1

    print('#{} {}'. format(tc, answer))