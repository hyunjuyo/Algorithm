import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(y, x):
    if y == M-1 and x == N-1:
        info[y][x] = 0
        return 1
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if info[y][x] == -1:
        info[y][x] = 0
        for i in range(4):
            ny = y + dir[i][0]
            nx = x + dir[i][1]
            if ny < 0 or ny >= M or nx < 0 or nx >= N:
                continue
            if table[y][x] > table[ny][nx]:
                info[y][x] += dfs(ny, nx)
    return info[y][x]

M, N = map(int, input().split())
table = []
for _ in range(M):
    table.append(list(map(int, sys.stdin.readline().split())))

info = [[-1] * N for _ in range(M)]

dfs(0, 0)
for v in info: # test
    print(v)

print(info[0][0])