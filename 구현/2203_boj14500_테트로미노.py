import sys

def check_shape(row, col, n, i, j):
    pos = []
    for (dy, dx) in shape[n]:
        ni = i + dy
        nj = j + dx
        if ni < 0 or ni >= row or nj < 0 or nj >= col:
            return False
        pos.append((ni, nj))
    return pos

def rotate_90(table, row, col):
    tmp_table = [[0] * row for _ in range(col)]
    for i in range(col):
        for j in range(row):
            tmp_table[i][j] = table[j][col - i - 1]
    return tmp_table, col, row

def get_max_num(table, n):
    max_list = []
    row, col = N, M
    for _ in range(4):
        table, row, col = rotate_90(table, row, col)
        tmp_max = 0
        for i in range(row):
            for j in range(col):
                pos = check_shape(row, col, n, i, j)
                if pos is False:
                    continue
                tmp = 0
                for (y, x) in pos:
                    tmp += table[y][x]
                tmp_max = max(tmp_max, tmp) # 가장 큰 값 저장
        max_list.append(tmp_max)
        # print(n, max_list) # test
    return max(max_list)

N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))

shape = [
    [(0, 0), (0, 1), (0, 2), (0, 3)], # 파랑
    [(0, 0), (0, 1), (1, 0), (1, 1)], # 노랑
    [(0, 0), (1, 0), (2, 0), (2, 1)], # 주황
    [(0, 1), (1, 1), (2, 1), (2, 0)], # 주황(대칭)
    [(0, 0), (1, 0), (1, 1), (2, 1)], # 연두
    [(0, 1), (1, 1), (1, 0), (2, 0)], # 연두(대칭)
    [(0, 0), (0, 1), (0, 2), (1, 1)] # 핑크
]

result = []
for n in range(7):
    max_num = get_max_num(table, n)
    result.append(max_num)

print(max(result))