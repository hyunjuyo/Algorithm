import sys
from collections import deque
sys.setrecursionlimit(100000)

def check_boundary(table):
    count = 0
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + dir[k][0]
                nj = j + dir[k][1]
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                diff = abs(table[i][j] - table[ni][nj])
                if diff >= L and diff <= R:
                    info[i][j].append((ni, nj))
                    tmp[i][j] = True
                    count += 1
    return count

def dfs(y, x):
    global pos
    pos.append((y, x))
    tmp[y][x] = False
    for (ny, nx) in info[y][x]:
        if tmp[ny][nx]:
            dfs(ny, nx)

# def bfs(y, x): # bfs로 할 경우 시간초과!!!!!
#     global pos
#     q = deque([(y, x)])
#     while q:
#         py, px = q.popleft()
#         if tmp[py][px]: # 중복 방지
#             pos.append((py, px))
#         tmp[py][px] = False
#         for (ny, nx) in info[py][px]:
#             if tmp[ny][nx]:
#                 q.append((ny, nx))

def fill_new_num(pos):
    total_sum = 0
    count = 0
    for i, j in pos:
        total_sum += table[i][j]
        count += 1
    new = total_sum // count
    for i, j in pos:
        table[i][j] = new

def open_n_move(table):
    global pos
    for i in range(N):
        for j in range(N):
            if tmp[i][j]:
                pos = []
                dfs(i, j)
                # print('-'*30) # test
                # print('pos :', pos) # test
                # for v in tmp: # test
                #     print(v)
                fill_new_num(pos)
                # for i, j in pos:
                #     table[i][j] = new_num

N, L, R = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0
tmp = [[False] * N for _ in range(N)]
while True:
    pos = []
    info = [[list() for _ in range(N)] for _ in range(N)]
    if check_boundary(table) == 0:
        break
    # print('here') # test
    # for v in tmp: # test
    #     print(v)
    # print(pos) # test
    open_n_move(table)
    # for v in table: # test
    #     print(v)
    result += 1

print(result)