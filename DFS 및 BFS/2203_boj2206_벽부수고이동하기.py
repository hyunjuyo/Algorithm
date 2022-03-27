import sys
from collections import deque

def bfs(y, x, s):
    q = deque([(y, x, s)])
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동, 남, 서, 북
    while q:
        py, px, s = q.popleft()
        for i in range(4):
            ny = py + d[i][0]
            nx = px + d[i][1]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if visited[ny][nx][s] > 0:
                continue
            if table[ny][nx] == 0:
                visited[ny][nx][s] = visited[py][px][s] + 1
                q.append((ny, nx, s))
            if table[ny][nx] == 1 and s == 0:
                visited[ny][nx][1] = visited[py][px][s] + 1
                q.append((ny, nx, 1))
        for ab in visited: # test
            for i, v in enumerate(zip(*ab)):
                for v2 in v:
                    if v2 < 10:
                        print(f'0{v2}', end=' ')
                    else:
                        print(v2, end=' ')
                if i == 0:
                    print(' |  ', end='')
            print()
        print('-'*50) # test

N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, list(sys.stdin.readline()[:-1]))))

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1 # 시작지점 count +1
bfs(0, 0, 0)

result = []
if visited[N-1][M-1][0] > 0:
    result.append(visited[N-1][M-1][0])
if visited[N-1][M-1][1] > 0:
    result.append(visited[N-1][M-1][1])

if result:
    print(min(result))
else:
    print(-1)