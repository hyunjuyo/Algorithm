import sys
from collections import deque
# sys.setrecursionlimit(10**6)

# def dfs(y, x): # 16% 지점 시간초과!!!!!
#     global count
#     if y == M-1 and x == N-1:
#         count += 1
#         return
#     dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     for i in range(4):
#         ny = y + dir[i][0]
#         nx = x + dir[i][1]
#         if ny < 0 or ny >= M or nx < 0 or nx >= N:
#             continue
#         if table[y][x] > table[ny][nx]:
#             dfs(ny, nx)

def bfs(y, x): # 20% 지점 시간초과!!!!!
    global count
    q = deque([(y, x)])
    while q:
        py, px = q.popleft()
        if py == M-1 and px == N-1:
            count += 1
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(4):
            ny = py + dir[i][0]
            nx = px + dir[i][1]
            if ny < 0 or ny >= M or nx < 0 or nx >= N:
                continue
            if table[py][px] > table[ny][nx]:
                q.append((ny, nx))

M, N = map(int, input().split())
table = []
for _ in range(M):
    table.append(list(map(int, sys.stdin.readline().split())))

count = 0
bfs(0, 0)

print(count)