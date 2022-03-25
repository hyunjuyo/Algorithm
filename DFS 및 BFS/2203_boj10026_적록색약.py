import sys
sys.setrecursionlimit(100000)

def dfs(table, y, x, color):
    table[y][x] = 0
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(4):
        ny = y + dir[i][0]
        nx = x + dir[i][1]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if table[ny][nx] == color:
            dfs(table, ny, nx, color)
    return table

N = int(input())
table_a = []
table_b = []
for _ in range(N):
    tmp = input()
    table_a.append(list(tmp))
    table_b.append(list(tmp.replace('G', 'R')))

count_a = 0
for i in range(N):
    for j in range(N):
        color = table_a[i][j]
        if color != 0:
            table_a = dfs(table_a, i, j, color)
            count_a += 1

count_b = 0
for i in range(N):
    for j in range(N):
        color = table_b[i][j]
        if color != 0:
            table_b = dfs(table_b, i, j, color)
            count_b += 1

print(count_a, count_b)