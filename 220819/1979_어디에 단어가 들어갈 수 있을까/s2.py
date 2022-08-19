# 1979_어디에 단어가 들어갈 수 있을까
# 2022-08-19

# 재승님 풀이 참고 wow!!
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if L[i][j] == 1:
                cnt1 += 1
            else:
                if cnt1 == K:
                    result += 1
                cnt1 = 0
            
            if L[j][i] == 1:
                cnt2 += 1
            else:
                if cnt2 == K:
                    result += 1
                cnt2 = 0
        
        if cnt1 == K:
            result += 1
        cnt1 = 0
        if cnt2 == K:
            result += 1 
        cnt2 = 0

    print('#{} {}'. format(tc, result))