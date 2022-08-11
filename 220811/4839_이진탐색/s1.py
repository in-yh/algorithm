# 4839_이진탐색
# 2022-08-11

import sys
sys.stdin = open('input.txt', 'r')

def binarySearch(a, N, key):
    start = 0
    end = N-1
    cnt = 1 # cnt 초기값은 while 밖에! 안에 넣으면 while문 돌 때마다 초기화 되니..
    while start <= end:
        center = int((start+end)/2)
        if a[center] == key:
            break
        elif a[center] > key:
            end = center # center-1이 아니라 center를 end에?
            cnt += 1
        elif a[center] < key:
            start = center # center+1이 아니라 center를 start에?
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split()) # P, Pa, Pb 
    
    cnt_Pa = binarySearch(list(range(1, P+1)), P, Pa)
    cnt_Pb = binarySearch(list(range(1, P+1)), P, Pb)

    if cnt_Pa < cnt_Pb:
        print('#{} A'. format(tc))
    elif cnt_Pa > cnt_Pb:
        print('#{} B'. format(tc))
    elif cnt_Pa == cnt_Pb:
        print('#{} 0'. format(tc))
