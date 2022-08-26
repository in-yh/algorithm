# 1230_암호문3
# 2022-08-26

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input()) # 원본 암호문의 길이
    origin = list(map(int, input().split())) # 원본 암호문
    M = int(input()) # 명령어 개수
    order = list(input().split()) # 명령어 
    for k in range(len(order)): # 'I', 'D', 'A'를 제외한 것은 int로 바꾸기
        if order[k] != 'I' and order[k] != 'D' and order[k] != 'A':
            order[k] = int(order[k])

    i = 0
    while i < len(order):
        if order[i] == 'I':
            for m in range(order[i+2]):
                origin.insert(order[i+1]+m, order[i+3+m])
            i += 3+order[i+2]
        elif order[i] == 'D':
            for _ in range(order[i+2]):
                origin.pop(order[i+1])
            i += 3
        elif order[i] == 'A':
            for o in range(order[i+1]):
                origin.append(order[i+2+o])
            i += 2+order[i+1]

    print('#{}'. format(tc), *origin[:10]) # 10개 출력하는 거를 못 봐서 오래걸림..