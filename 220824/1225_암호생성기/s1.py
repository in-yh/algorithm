# 1225_암호생성기
# 2022-08-24

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    q = list(map(int, input().split()))

    i = 1
    while q[0]-i > 0: # (첫 원소-i)가 0보다 클 때, (pop(0)한 원소-i)를 맨 뒤에 추가해줌
        a = q.pop(0)
        q.append(a-i)
        if i < 5: # i는 1부터 5가 반복되게 설정
            i += 1
        else:
            i = 1
    q.pop(0) # (pop한 원소-i)가 0보다 작거나 같다면, 0으로 유지 및 프로그램 종료 
    q.append(0)
    
    print('#{}'. format(tc), *q)