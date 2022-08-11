# 4843_특별한 정렬
# 2022-08-11

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))

    for i in range(0, 10): # 다 정렬하려면 N-1까지이지만, 10개만 print하라고 했으므로 10까지 함.
        if i%2 == 0: # i가 짝수일 때 / 최대값 구하기
            maxIdx = i # i가 기준값 / Value가 아닌 Idx를 i로 설정해야 함.(Value로 설정하면 자리 바꿀 때 max값도 바뀜)
            for j in range(i+1, N): # j를 i+1부터 N까지 돌려줌(i 이후와의 비교를 위해 i+1로 설정)                
                if L[j] > L[maxIdx]:                     
                    maxIdx = j 
            L[i], L[maxIdx] = L[maxIdx], L[i] # for문 바깥으로 빼줘야 j가 다 순회하고 마지막에 바꿔줌(for문 안에 넣으면 L이 계속 바뀌기 때문에 정렬이 아주 이상하게 됨..)
        else: # i가 홀수일 때 / 최소값 구하기
            minIdx = i
            for j in range(i+1, N):
                if L[j] < L[minIdx]:
                    minIdx = j
            L[i], L[minIdx] = L[minIdx], L[i] 

    print('#{}'. format(tc), *L[0:10]) # 10개만 추출