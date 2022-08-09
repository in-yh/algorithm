# 연습문제2_Baby-Gin
# 2022-08-08

T = int(input())
for t in range(1, T+1):

    arr = list(map(int, input()))
    tri = run  = 0
    c = [0] * 10

    for i in range(6):
        c[arr[i]] += 1

    j = 0
    while j < 10:
        if c[j] >= 3:
            tri += 1
            c[j] -= 3
            continue
        if c[j] >= 1 and c[j+1] >= 1 and c[j+2] >= 1: # 3가지 조건 다 넣기
            run += 1
            c[j] -= 1
            c[j+1] -= 1
            c[j+2] -= 1
            continue
        j += 1 # 여기에 +1 해주면 같은 j도 한 번 더 if문을 들어갈 수 있음.

    if tri + run == 2:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')