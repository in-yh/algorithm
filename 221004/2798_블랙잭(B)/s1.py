# 2798_블랙잭(B)
# 2022-10-03

import sys
sys.stdin = open('input.txt', 'r')

def nCr(n, r, s):
    if r == 0:
        result.append(comb[:]) # 내용만 복사 해줘야 함
        return
    else:
        for i in range(s, n-r+1):
            comb[r-1] = cards[i]
            nCr(n, r-1, i+1)


N, M = map(int, input().split())
cards = list(map(int, input().split()))
comb = [0]*3
result = []
nCr(N, 3, 0)

maxV = 0
for r in result:
    if sum(r) <= M:
        if maxV < sum(r):
            maxV = sum(r)
print(maxV)