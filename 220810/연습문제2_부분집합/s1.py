# 연습문제2_부분집합
# 2022-08-10

import sys
sys.stdin = open('input.txt', 'r')

def length(my_list):
    cnt = 0
    for _ in my_list:
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = length(arr) # n : 원소의 개수(10)

    s = [0]*(1<<n)
    for i in range(1<<n): # 1<<n : 부분 집합 개수
        for j in range(n):
            if i & (1<<j):
                s[i] += arr[j]
    
    if 0 in s[1:]: # s[0]은 공집합으로 무조건 0이니깐 빼고 탐색 / in 사용 안하고 할 수 없을까.. 함수를 만들까..
        print('#{} 1'. format(tc))
    else:
        print('#{} 0'. format(tc))


        
        