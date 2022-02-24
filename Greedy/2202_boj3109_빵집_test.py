import sys

def dfs(py, px, order):
    global count

    table[py][px] = 'o' # 파이프 연결
    if px == C:
        count += 1

    # 북동, 동, 남동
    dir_x = [1, 1, 1]
    dir_y = [-1, 0, 1]

    for i in range(3):
        if order == 0: # 위쪽부터 탐색
            nx = px + dir_x[i]
            ny = py + dir_y[i]
        else: # 아래쪽부터 탐색
            nx = px + dir_x[2-i]
            ny = py + dir_y[2-i]

        # print(py, px, '=>', ny, nx) # test
        # 범위 벗어나거나 건물 또는 이미 연결한 파이프라인 있는 경우
        if nx < 1 or nx > C or ny < 1 or ny > R or table[ny][nx] == 'x' or table[ny][nx] == 'o':
            continue
        else:
            table[ny][nx] = 'o' # 파이프 연결
            dfs(ny, nx, order)
            if nx == C:
                return
            # return # 한 번에 하나의 파이프라인만 연결

R, C = map(int, input().split())

table_org = [['0'] * (C+1)]
for _ in range(R):
    table_org.append(list('0' + sys.stdin.readline()[:-1]))

# for v in table: # test
#     print(v)

count_list = []
for order in range(2):
    table = [row[:] for row in table_org] # 복사본 생성
    count = 0
    for i in range(1, R+1):
        if order != 0:
            i = R - i + 1
        dfs(i, 1, order)
    count_list.append(count)

    for v in table: # test
        print(v)
    print('-'*50) # test

# count = 0
# for i in range(1, R+1):
#     if table[i][C] == 'o':
#         count += 1

print(count_list) # test

print(max(count_list))