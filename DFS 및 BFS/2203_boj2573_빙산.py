import sys
from collections import deque
sys.setrecursionlimit(100000)

def bfs(pos_list):
    next_pos_list = []

    q = deque(pos_list)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dir[i][0]
            nx = x + dir[i][1]
            if snapshot[ny][nx] == 0: # 한 면이 바다일 경우
                table[y][x] -= 1
        if table[y][x] <= 0:
            table[y][x] = 0
        else:
            next_pos_list.append((y, x)) # 남아있는 빙산 위치 저장
    
    return next_pos_list

def dfs(tmp_table, y, x):
    tmp_table[y][x] = 0
    for i in range(4):
        ny = y + dir[i][0]
        nx = x + dir[i][1]
        # print(f'({y}, {x}) -> ({ny}, {nx})') # test
        if tmp_table[ny][nx] > 0:
            dfs(tmp_table, ny, nx)

def is_complete(table):
    count = 0
    tmp_table = [row[:] for row in table] # 복사본 생성

    for i in range(N):
        for j in range(M):
            if tmp_table[i][j] > 0:
                dfs(tmp_table, i, j)
                count += 1

    if count == 1:
        return False
    else:
        return True

N, M = map(int, input().split())

table = []
for _ in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))

# 빙산 위치 저장
pos_list = []
for i in range(N):
    for j in range(M):
        if table[i][j] > 0:
            pos_list.append((i, j))

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서

period = 0
while pos_list:
    print(f'year {period + 1}', '-'*50) # test
    print('pos_list :', pos_list) # test
    snapshot = [row[:] for row in table] # 현 상태 복사본 생성
    pos_list = bfs(pos_list)

    for v in table: # test
        print(v)

    period += 1
    if is_complete(table):
        break

if pos_list:
    print(period)
else:
    print(0)