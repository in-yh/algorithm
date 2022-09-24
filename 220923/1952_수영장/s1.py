# 1952_수영장
# 2022-09-23

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    
    # 1년권 했을 때 금액 구해줌
    year_price = price[3]

    # 1일권, 1달권, 3개월권을 dp로..
    dp = [0]*13 
    for idx, p in enumerate(plan, start=1):
        dp[idx] = min(p*price[0], price[1]) + dp[idx-1] # dp 리스트에 합을 넣어주고, 0인덱스는 비워줌

        if idx >= 3: # 3월부터 3개월권 비교
            dp[idx] = min(dp[idx], price[2]+dp[idx-3])
    
    answer = min(dp[12], year_price)

    print('#{} {}'.format(tc, answer))