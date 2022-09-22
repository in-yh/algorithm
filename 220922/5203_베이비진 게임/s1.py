# 5203_베이비진 게임
# 2022-09-22

import sys
sys.stdin = open('input.txt', 'r')

def baby_gin(arr):
    cnt = [0]*10
    for m in range(len(arr)):
        cnt[arr[m]] += 1
    
    tris = 0
    runs = 0
    n = 0
    while n<10:
        if cnt[n] >= 3:
            cnt[n] -= 3
            tris += 1
            continue
        if n < 8 and cnt[n] >= 1 and cnt[n+1] >= 1 and cnt[n+2] >= 1:
            cnt[n] -= 1
            cnt[n+1] -= 1
            cnt[n+2] -= 1
            runs += 1
            continue
        n += 1
    
    return tris+runs


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    for i in range(12):
        if i%2==0: # 플레이어 1
            player1.append(cards[i])
        else:
            player2.append(cards[i])
    
        # '6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.' 라는 조건이 있음
        if baby_gin(player1) > baby_gin(player2):
            result = 1
            break
        elif baby_gin(player1) < baby_gin(player2):
            result = 2
            break
        elif baby_gin(player1) == baby_gin(player2):
            result = 0

    print('#{} {}'.format(tc, result))