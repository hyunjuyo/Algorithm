from itertools import combinations

def get_cand_list(table):
    cand_list = []
    for i in range(N):
        for j in range(M):
            if table[i][j] == 0:
                cand_list.append((i, j))
    return cand_list

def dfs_safe(y, x, tb):
    global area
    tb[y][x] = 9 # 방문지점 표시
    area += 1 # 크기 정보 +1
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(4):
        ny = y + dir[i][0]
        nx = x + dir[i][1]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if tb[ny][nx] == 0: # 안전영역일 경우
            dfs_safe(ny, nx, tb)

def get_safe_area(tb):
    global area
    safe_area = []
    for i in range(N):
        for j in range(M):
            if tb[i][j] == 0:
                area = 0
                dfs_safe(i, j, tb)
                safe_area.append(area) # 안전영역 크기 정보 담기
    return safe_area

def dfs_virus(y, x, tb):
    tb[y][x] = 2 # 방문지점 표시
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(4):
        ny = y + dir[i][0]
        nx = x + dir[i][1]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if tb[ny][nx] == 0:
            dfs_virus(ny, nx, tb)

def check_virus(tb):
    for i in range(N):
        for j in range(M):
            if tb[i][j] == 2:
                dfs_virus(i, j, tb)
    return tb

N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

# 벽을 세울 수 있는 위치정보(후보) 저장
cand_list = get_cand_list(table)

result = 0
for cand in combinations(cand_list, 3):
    tmp_table = [row[:] for row in table] # 복사본 생성

    # 벽 3개 세우기
    tmp_table[cand[0][0]][cand[0][1]] = 1
    tmp_table[cand[1][0]][cand[1][1]] = 1
    tmp_table[cand[2][0]][cand[2][1]] = 1

    # 바이러스 전파 상황 반영
    tmp_table = check_virus(tmp_table)
    # print('-'*30) # test
    # for v in tmp_table: # test
    #     print(v)

    area = 0
    safe_area = get_safe_area(tmp_table) # 안전영역 크기 정보 list 저장
    if safe_area:
        # tmp = result # test
        result = max(result, sum(safe_area)) # 가장 큰 영역크기로 업데이트
        # if tmp != result: # test
        #     print('cand :', cand) # test
        #     print('safe_area :', safe_area) # test
        #     for v in tmp_table: # test
        #         print(v)
        #     print('-'*30) # test

print(result)