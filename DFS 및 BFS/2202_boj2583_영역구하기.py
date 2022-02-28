import sys
from collections import deque

sys.setrecursionlimit(100000) # 셋팅 필요 !!!!!

def draw_rectangle(c1, r1, c2, r2):
    for row in range(M):
        for col in range(N):
            if row >= r1 and row < r2 and col >= c1 and col < c2:
                table[row][col] = 1

def dfs(row, col):
    global area
    table[row][col] = 1

    # 북, 동, 남, 서
    dir_x = [0, 1, 0, -1]
    dir_y = [-1, 0, 1, 0]

    px = col
    py = row
    for i in range(4):
        nx = px + dir_x[i]
        ny = py + dir_y[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if table[ny][nx] == 0:
            area += 1
            dfs(ny, nx)

M, N, K = map(int, input().split())

table = [[0] * (N) for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    draw_rectangle(x1, y1, x2, y2)

count = 0
area_list = []
for i in range(M):
    for j in range(N):
        if table[i][j] == 0:
            count += 1
            area = 1
            dfs(i, j)
            area_list.append(area)

area_list.sort()

print(count)
for v in area_list:
    print(v, end=' ')