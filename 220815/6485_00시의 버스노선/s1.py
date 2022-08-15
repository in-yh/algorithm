# 6485_00시의 버스노선
# 2022-08-15

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    bus_stop = [0]*5001 # 버스정류장 1~5000개, 5001개로 하여 인덱스 헷갈림 방지
    N = int(input()) # 버스노선 N개
    for n in range(1, N+1): 
        A, B = map(int, input().split()) 
        for i in range(A, B+1): # 노선 범위(A~B) 안에 있는 정류소 +1씩 해줌, 이렇게 for문 돌리니 런타임에러 안나네..
            bus_stop[i] += 1

    P = int(input()) # 출력해야할 버스정류장 개수
    L = []
    for _ in range(1, P+1): # 1~5
        C = int(input()) # 1
        L.append(bus_stop[C]) # bus_stop[1] 추가

    print('#{}'. format(tc), *L)