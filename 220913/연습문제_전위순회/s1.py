# 연습문제_전위순회
# 2022-09-13

import sys
sys.stdin = open('input.txt', 'r')

def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0: # 부모가 없으면 root
            return i

def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


V = int(input()) # 정점 개수, 마지막 정점번호
E = V-1 # 간선 개수
L = list(map(int, input().split()))
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
par = [0]*(V+1)
for i in range(0, 2*E, 2):
    p, c = L[i], L[i+1]

    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

    par[c] = p

root = find_root(V)

preorder(root)