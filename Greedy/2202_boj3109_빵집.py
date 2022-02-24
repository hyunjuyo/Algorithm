import sys

def dfs(py, px):
    global count, flag
    if flag == True:
        return

    table[py][px] = 'o' # 파이프 연결
    if px == C:
        count += 1
        flag = True
        return

    # 북동, 동, 남동
    dir_x = [1, 1, 1]
    dir_y = [-1, 0, 1]

    for i in range(3):
        nx = px + dir_x[i]
        ny = py + dir_y[i]

        # 범위 벗어나거나 건물 또는 이미 연결한 파이프라인 있는 경우
        if nx < 1 or nx > C or ny < 1 or ny > R or table[ny][nx] == 'x' or table[ny][nx] == 'o':
            continue
        else:
            dfs(ny, nx)
            if nx == C:
                return

R, C = map(int, input().split())

table = [['0'] * (C+1)]
for _ in range(R):
    table.append(list('0' + sys.stdin.readline()[:-1]))

count = 0
for i in range(1, R+1):
    flag = False
    dfs(i, 1)

# for v in table: # test
#     print(v)
# print('-'*50) # test

print(count)