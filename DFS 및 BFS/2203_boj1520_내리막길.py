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

def bfs_l(y, x, row):
    global count
    q = deque([(y, x)])
    while q:
        py, px = q.popleft()
        if py == row and px == lth-1: # 중간지점
            count += 1
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(4):
            ny = py + dir[i][0]
            nx = px + dir[i][1]
            if ny < 0 or ny >= M or nx < 0 or nx >= lth: # 왼쪽 테이블 범위 반영
                continue
            if table_l[py][px] > table_l[ny][nx]:
                q.append((ny, nx))

def bfs_r(y, x):
    global count
    q = deque([(y, x)])
    while q:
        py, px = q.popleft()
        if py == M-1 and px == N-lth-1: # 도착지점
            count += 1
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(4):
            ny = py + dir[i][0]
            nx = px + dir[i][1]
            if ny < 0 or ny >= M or nx < 0 or nx >= N-lth: # 오른쪽 테이블 범위 반영
                continue
            if table_r[py][px] > table_r[ny][nx]:
                q.append((ny, nx))

def bfs(y, x):
    global total_count
    q = deque([(y, x)])
    while q:
        py, px = q.popleft()
        if py == M-1 and px == N-1:
            total_count += 1
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

total_count = 0
if N < 3:
    bfs(0, 0)
else:
    lth = N // 2 # 분리 후 왼쪽 테이블의 열 길이

    table_l = [] # 왼쪽 테이블
    for i in range(M):
        table_l.append(table[i][:lth])
    table_r = [] # 오른쪽 테이블
    for i in range(M):
        table_r.append(table[i][lth:])

    print('table_l') # test
    for v in table_l: # test
        print(v)
    print('table_r') # test
    for v in table_r: # test
        print(v)

    count_l = [0] * M
    count_r = [0] * M
    for i in range(M):
        count = 0
        bfs_l(0, 0, i)
        count_l[i] = count

        count = 0
        bfs_r(i, 0)
        count_r[i] = count

    print('count_l :', count_l) # test
    print('count_r :', count_r) # test

    for i in range(M):
        total_count += count_l[i] * count_r[i]

print(total_count)