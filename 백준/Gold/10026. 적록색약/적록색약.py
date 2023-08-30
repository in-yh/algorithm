N = int(input())
picture = [list(map(str, input())) for _ in range(N)]

def bfs1(si, sj, a):
    visited1[si][sj] = a
    stack.append((si, sj))
    while stack:
        n, m = stack.pop(0)
        for dn, dm in [[0,1],[1,0],[0,-1],[-1,0]]:
            nn, nm = n+dn, m+dm
            if 0<=nn<N and 0<=nm<N and picture[nn][nm]==picture[n][m] and visited1[nn][nm]==0:
                visited1[nn][nm] = visited1[n][m]
                stack.append((nn, nm))

def bfs2(si, sj, a):
    visited2[si][sj] = a
    stack.append((si, sj))
    while stack:
        n, m = stack.pop(0)
        for dn, dm in [[0,1],[1,0],[0,-1],[-1,0]]:
            nn, nm = n+dn, m+dm
            if 0<=nn<N and 0<=nm<N and visited2[nn][nm]==0: 
                if picture[n][m]=='B':
                    if picture[nn][nm]=='B':
                        visited2[nn][nm] = visited2[n][m]
                        stack.append((nn, nm))
                else:
                    if picture[nn][nm]!='B':
                        visited2[nn][nm] = visited2[n][m]
                        stack.append((nn, nm))


# 일반인
visited1 = [[0]*N for _ in range(N)] 
stack = []

k=1
for i in range(N):
    for j in range(N):
        if visited1[i][j] == 0:
            bfs1(i, j, k)
            k += 1

answer1 = 0     
for v in visited1:
    answer1 = max(max(v), answer1)


# 적록색약
visited2 = [[0]*N for _ in range(N)]

l=1
for i in range(N):
    for j in range(N):
        if visited2[i][j] == 0:
            bfs2(i, j, l)
            l += 1

answer2 = 0     
for v in visited2:
    answer2 = max(max(v), answer2)

print(answer1, answer2)