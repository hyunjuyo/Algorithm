import sys
from collections import deque

def is_cand(table, y, x):
    count_zero = 0
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(4):
        ny = y + d[i][0]
        nx = x + d[i][1]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if table[ny][nx] == 0:
            count_zero += 1
    if count_zero >= 2:
        return True
    else:
        return False

def get_cand(table):
    pos = []
    for i in range(N):
        for j in range(M):
            if table[i][j] == 1 and is_cand(table, i, j):
                pos.append((i, j))
    return pos

def bfs(y, x):
    q = deque([(y, x)])
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        py, px = q.popleft()
        for i in range(4):
            ny = py + d[i][0]
            nx = px + d[i][1]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if table[ny][nx] == 0:
                table[ny][nx] = table[py][px] + 1
                q.append((ny, nx))
        for v in table: # test
            print(v)
        print('-'*20) # test

N, M = map(int, input().split())
table_org = []
for _ in range(N):
    table_org.append(list(map(int, list(sys.stdin.readline()[:-1]))))

pos = get_cand(table_org)
print('pos :', pos) # test

result = []
for (y, x) in pos:
    print(f'({y}, {x})', '-'*20) # test
    table = [row[:] for row in table_org] # 복사본 생성
    table[y][x] = 0 # 벽 부수기

    table[0][0] = 1 # 시작지점 count +1
    bfs(0, 0)
    if table[N-1][M-1] > 0:
        result.append(table[N-1][M-1])

print(result) # test
if result:
    print(min(result))
else:
    print(-1)