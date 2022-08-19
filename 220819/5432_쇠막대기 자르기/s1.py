# 5432_쇠막대기 자르기
# 2022-08-19

# result = +3  3(현개수 3, 여는괄호 3)(레이저 만남) 
# result = +3  3(현개수 3)(레이저 만남)
# result = +1  (닫는괄호, 현개수 -1 되어 2) 
# result = +3  3(현개수 3, 여는괄호 1)(레이저 만남)
# result = +1  (닫는괄호, 현개수 -1 되어 2) 
# result = +2  2(현개수)(레이저만남)
# result = +2  2(닫는괄호 2, 현개수 -2되어 0)
# result = +1  1(현개수 1, 여는괄호 1)(레이저 만남)
# result = +1  (닫는괄호 개수)

# 세줄 요약
# 여는괄호 만나고 바로 닫는괄호를 만나지 않으면 현개수 +1, 
# 여는괄호 바로 뒤에 닫는괄호 만나면 레이저, 레이저 만나면 result += 현개수
# 닫는괄호 만나면 현개수 -1, result += 1

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    s = input()
    result = 0 # 잘려진 조각의 총 개수 초기값
    now = 0 # 현재 놓여져 있는 쇠막대기 수
    i = 0

    while i < len(s):
        if i < len(s)-1 and s[i] == '(' and s[i+1] != ')':
            now += 1
            i += 1
        elif i < len(s)-1 and s[i] == '(' and s[i+1] == ')':
            result += now
            i += 2
        elif s[i] == ')':
            now -= 1
            result += 1
            i += 1

    print('#{} {}'. format(tc, result))