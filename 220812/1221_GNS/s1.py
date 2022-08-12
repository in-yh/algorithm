# 1221_GNS
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

T = int(input())
for _ in range(1, T+1):
    tc, N = input().split() # tc = "#1", N = "7041"
    N = int(N) # N = 7041 / 숫자로 바꿔줌
    L = list(map(str, input().split())) # ["SVN", "FOR", "ZRO", "NIN", ...]

	# L과 같은지 비교할 문자로 된 기준 리스트
    str_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
	# L을 순회하면서 기준 리스트의 특정 원소와 같다면 그 인덱스(숫자)를 아래 리스트에 저장, 숫자로 저장하는 이유는 크기별로 정렬시켜줘야 하기 때문
    new_list = []

    for i in range(N): # L의 개수 : 7041
        for j in range(10): # str_to_int의 개수 : 10
            if L[i] == str_num[j]:
                new_list.append(j)
                break
    # new_list = [7, 4, 0, ...]

    # 작은 숫자가 작은 쪽으로 오게끔 정렬 (선택정렬) / new_list = [0, 0, ...] 만들기
    for k in range(N-1): # k = 0 ~ N-2
        minIdx = k # k가 기준값
        for l in range(k+1, N): # l = k+1 ~ N 
            if new_list[minIdx] > new_list[l]: # 7 > 4 / 4 > 0
                minIdx = l # minIdx를 0에서 1로 바꿔줘 / 1에서 2로 바꿔줘
        new_list[k], new_list[minIdx] = new_list[minIdx], new_list[k]

    # 정렬된 숫자 리스트를 문자 리스트로 변경
    for m in range(N):
        new_list[m] = str_num[new_list[m]] # ["ZRO", "ZRO", ...]

    print('{}'. format(tc))
    print(*new_list)