# 5207_이진 탐색
# 2022-09-27

import sys
sys.stdin = open('input.txt', 'r')

def BinarySearch(l, r, key):
    global cnt
    while l<=r: # 이 범위 설정 조심!!
        mid = (l+r)//2
        if key == N_list[mid]:
            cnt.append(0)
            return
        elif key > N_list[mid]:
            l = mid+1
            cnt.append(1)
        elif key < N_list[mid]:
            r = mid-1
            cnt.append(2)
    cnt = []
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    N_list.sort() # 이진탐색할 때는 sort 반드시!!
    
    result = 0
    for m in M_list:
        cnt = []
        BinarySearch(0, N-1, m)
        if len(cnt)==1:
            result += 1
        elif len(cnt)>=2:
            for i in range(len(cnt)-1): # 연속이 하나라도 있다면
                if cnt[i] == cnt[i+1]:
                    break
            else: # 연속이 하나도 없다면
                result += 1
    
    print('#{} {}'.format(tc, result))