# 1859_백만장자 프로젝트
# 2022-08-19

import sys
sys.stdin = open('input.txt', 'r')

def max_idx_value(length, lists):
    idx = 0
    for i in range(1, length):
        if lists[idx] < lists[i]:
            idx = i
    return idx, lists[idx]


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 5
    price = list(map(int, input().split())) # 6426 9445 8772 81 3447

    # 선택정렬(오늘 사서 오른쪽 값이 오늘값보다 크면서 가장 최대값일 때 팔아라) 너무 오래 걸림.. 그렇다면..
    # 정렬 순회 후 max 값과 인덱스를 찾고, max 인덱스의 왼쪽값은 다 빼고 왼쪽 개수*max값을 더해준다.
    # max 인덱스 이후부터 max 값 찾아주고 위를 반복한다.

    total_sums = 0
    while N > 0:
        index = max_idx_value(N, price)[0] # 1
        value = max_idx_value(N, price)[1] # 9445

        sums1 = 0
        for i in range(index):
            sums1 -= price[i]
        sums2 = index * value

        total_sums += sums1 + sums2

        N = N-(index+1)
        price = price[(index+1):]

    print('#{} {}'. format(tc, total_sums))