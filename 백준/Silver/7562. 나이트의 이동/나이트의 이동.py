tc = int(input())

def bfs(i, j, k, l, length):
    global answer
    visited[i][j] = 0
    stack.append((i, j))
    while stack:
        n, m = stack.pop(0)
        for dn, dm in [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]:
            nn, nm = n+dn, m+dm
            if 0<=nn<length and 0<=nm<length and nn==k and nm==l:
                visited[nn][nm] = visited[n][m] + 1
                answer = visited[nn][nm]
                return
            elif 0<=nn<length and 0<=nm<length and visited[nn][nm]==0:
                visited[nn][nm] = visited[n][m] + 1
                stack.append((nn, nm))

result = []
for _ in range(tc):
    length = int(input())
    si, sj = map(int, input().split())
    fk, fl = map(int, input().split())

    visited = [[0]*length for _ in range(length)]
    stack = []
    answer = 0

    if si==fk and sj==fl:
        result.append(0)
    else:
        bfs(si, sj, fk, fl, length)
        result.append(answer)

for r in result:
    print(r)