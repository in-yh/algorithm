# 4837_부분집합의 합
# 2022-08-11

import sys
sys.stdin = open('input.txt', 'r')

def sum_list(list_1):
    s = 0
    for i in list_1:
        s += i
    return s

def len_list(list_2):
    l = 0
    for j in list_2:
        l += 1
    return l

T = int(input())
for tc in range(1, T+1):
    A = list(range(1, 13)) # 1부터 12까지의 숫자를 가진 A
    length_A = 12 # A의 길이

    N, K = map(int, input().split()) # 부분집합 내 원소 개수, 부분집합의 합 

    subset_total = [0]* (1<<length_A)
    for i in range(1<<length_A): # 부분집합의 개수(2^12)만큼 i 돌려줌
        subset = []
        for j in range(length_A): # 원소의 수만큼 j 돌려줌
            if i & (1<<j): # i의 j번째가 1이라면,
                subset.append(A[j]) # 각각의 부분집합을 subset에 묶어줌
        subset_total[i] = subset # 각각의 부분집합 subset를 subset_total에 넣어줌, subset_total는 모든 부분집합을 모아놓은 리스트임

    cnt = 0
    for i in range(1<<length_A):
        if len_list(subset_total[i]) == N and sum_list(subset_total[i]) == K:
            cnt += 1
    
    print('#{} {}'. format(tc, cnt))