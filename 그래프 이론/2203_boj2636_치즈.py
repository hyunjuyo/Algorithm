import sys
sys.setrecursionlimit(10**6)

def dfs_air(y, x):
    table[y][x] = 9 # 9로 표기
    for v in dr:
        ny = y + v[0]
        nx = x + v[1]
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            continue
        if table[ny][nx] == 1:
            one_pos.add((ny, nx))
        if table[ny][nx] == 0:
            dfs_air(ny, nx)

def dfs_count(y, x):
    table[y][x] = 9
    for v in dr:
        ny = y + v[0]
        nx = x + v[1]
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            continue
        if table[ny][nx] == 1:
            dfs_count(ny, nx)

R, C = map(int, input().split())
cheese = 0 # 치즈 개수 저장용
table = []
for _ in range(R):
    tmp = list(map(int, input().split()))
    table.append(tmp)
    cheese += sum(tmp) # 치즈 개수 업데이트

dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 공기 부분 9로 표기
one_pos = set()
dfs_air(0, 0)

hour = 0
while True:
    if len(one_pos) == cheese: # 치즈가 모두 녹기 한 시간 전일 경우
        break

    # 새로 공기 접촉한 0 위치 정보 저장
    zero_pos = set()
    for (y, x) in one_pos:
        for v in dr:
            ny = y + v[0]
            nx = x + v[1]
            if table[ny][nx] == 0: # 새로 공기 접촉하게 된 경우
                zero_pos.add((ny, nx))

    # 치즈가 녹는다
    for (y, x) in one_pos:
        table[y][x] = 9
        cheese -= 1 # 현재 치즈 개수 업데이트

    # 현재 기준 공기 부분 9로 표기
    for (y, x) in zero_pos:
        dfs_air(y, x)

    # 공기와 접촉한 1 위치 저장
    one_pos = set()
    for i in range(R):
        for j in range(C):
            if table[i][j] == 1:
                for v in dr:
                    ni = i + v[0]
                    nj = j + v[1]
                    if table[ni][nj] == 9:
                        one_pos.add((i, j))
                        break

    hour += 1

print(hour + 1)
print(cheese)