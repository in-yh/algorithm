# 2115_벌꿀채취
# 2022-09-30

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    assemble = [] # 좌표, 그 좌표부터 M개까지의 벌통에서 C보다 작으면 제곱의 합 저장하고 C보다 크면 특정 수 제거하고 남은 수들의 제곱의 합 중 가장 큰 값 저장 
    for i in range(0, N): # 모든 경우의 수 찾기
        for j in range(0, N-M+1):
            answer = 0
            if sum(honey[i][j:j+M]) <= C:
                for k in range(j, j+M):
                    answer += (honey[i][k])**2
            else:
                a = honey[i][j:j+M] # 부분집합 모두 구한 후 합이 C보다 작은 값 중 제곱의 합이 가장 큰 값을 answer에 넣자
                for m in range(1, 1<<len(a)):
                    subset = []
                    for n in range(len(a)):
                        if m & (1<<n):
                            subset.append(a[n])
                    if sum(subset) <= C:
                        tmp = 0
                        for s in subset:
                            tmp += s**2
                        answer = max(answer, tmp)                     
                
            assemble.append((i, j, answer))
    assemble.sort(key=lambda x:x[2], reverse=True) # answer이 큰 것부터 정렬

    # 두명의 일꾼이므로 두개 선택하여 최종값 산출하기(answer이 가장 큰 맨 처음 값과 행 다르거나 행이 같더라도 열 겹치지 않는 두개 선택)
    result = assemble[0][2]
    i = 1
    while True:
        if assemble[0][0] != assemble[i][0]:
            result += assemble[i][2]
            break
        else: # 행이 같다면
            if assemble[0][1]+M-1 < assemble[i][1] or assemble[0][1] > assemble[i][1]+M-1: # 근데 열이 겹치지 않아 / 
                result += assemble[i][2]
                break
            else: # 열이 또 겹쳐 -> 그럼 다음으로 넘어가 반복
                i += 1
    print('#{} {}'.format(tc, result))