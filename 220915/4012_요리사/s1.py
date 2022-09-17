# 4012_요리사
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')

def combination(L, n): # len(L)Cn
    result = []
    if n == 0: # 하나도 뽑지 않을 때 빈이중리스트로 리턴
        return [[]]

    for i in range(len(L)):
        elem = L[i]
        for rest in combination(L[i+1:], n-1): # 여기서 재귀.. / L[i+1:]해도 인덱스 에러 나지 않음
            result.append([elem] + rest)
    return result


def permutation(L, n): # len(L)Pn
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(L)):
        elem = L[i]
        for rest in permutation(L[:i]+L[i+1:], n-1):
            result.append([elem] + rest)
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 식재료수
    S = [list(map(int, input().split())) for _ in range(N)] # 재료간 시너지

    # 식재료수를 둘로 나누는 건 조합 이용 / 식재료수가 6개면 (6//2)개씩 나눔(6C(6//2)개)
    # 6C3번 for문을 돌려주고 A음식(S[0][1] + S[0][2] + S[1][0] + S[1][2] + S[2][0] + S[2][1]) / B음식  =>  각각 (6//2)P2 (순열)
    veget = list(range(N)) # [0, 1, 2, 3, 4, 5]
    A_veget_combi = combination(veget, N//2)
    
    total_S = 0 # 2차원리스트 S 총합으로 minV 초기값 설정
    for s in S:
        total_S += sum(s)
    minV = total_S

    for i in range(len(A_veget_combi)): # 6C3번(20번)
        B_veget_combi = list(set(veget)-set(A_veget_combi[i])) # B는 veget에서 A의 원소 제거하여 구하기(set이용)

        A_veget_perm = permutation(A_veget_combi[i], 2) # len(A_veget_combi[i])P2
        B_veget_perm = permutation(B_veget_combi, 2)

        A = 0
        B = 0
        for j in range(len(A_veget_perm)):
            A += S[A_veget_perm[j][0]][A_veget_perm[j][1]]
            B += S[B_veget_perm[j][0]][B_veget_perm[j][1]]

        if minV > abs(A-B):
            minV = abs(A-B)
        
    print('#{} {}'. format(tc, minV))