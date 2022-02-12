import sys
from collections import deque

def bfs(i, j):
    tmp_table[i][j] = 0 # 시작지점 구분을 위해 0 입력

    # 북, 동, 남, 서
    dir_i = [-1, 0, 1, 0]
    dir_j = [0, 1, 0, -1]

    q = deque([(i, j)])

    while q:
        pi, pj = q.popleft()

        for idx in range(4):
            ni = pi + dir_i[idx]
            nj = pj + dir_j[idx]
            if ni < 0 or ni >= R or nj < 0 or nj >= C or tmp_table[ni][nj] == -2: # 범위를 벗어나거나 바다인 경우
                continue
            if tmp_table[ni][nj] == -1: # 육지인 경우
                q.append((ni, nj))
                tmp_table[ni][nj] = tmp_table[pi][pj] + 1

def get_max_num(table):
    max_num = -1

    for row in table:
        tmp = max(row)
        if max_num < tmp:
            max_num = tmp
    
    return max_num

R, C = map(int, input().split())

table = []
for _ in range(R):
    table.append(list(sys.stdin.readline())[:C])

# 숫자로 변환
for i in range(R):
    for j in range(C):
        if table[i][j] == 'L':
            table[i][j] = -1
        else:
            table[i][j] = -2

max_num_list = []
for i in range(R):
    for j in range(C):
        if table[i][j] == -1:
            tmp_table = [row[:] for row in table] # table 복사본 생성
            bfs(i, j)
            max_num_list.append(get_max_num(tmp_table))

# print(len(max_num_list)) # test
# print(max_num_list) # test

print(max(max_num_list))