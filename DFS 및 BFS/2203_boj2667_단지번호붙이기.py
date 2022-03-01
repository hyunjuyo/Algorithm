import sys
sys.setrecursionlimit(100000)

def dfs(y, x):
    global count
    table[y][x] = 0 # 방문 시 0 입력
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서

    for i in range(4):
        ny = y + dir[i][0]
        nx = x + dir[i][1]
        if ny < 0 or ny >= N or nx < 0 or nx >= N or table[ny][nx] == 0:
            continue
        else:
            count += 1
            dfs(ny, nx)

N = int(input())
table = [list(map(int, list(input()))) for _ in range(N)]

count_list = []
for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            count = 1
            dfs(i, j)
            count_list.append(count)

# print(count_list) # test
count_list.sort()

print(len(count_list))
print(*count_list, sep='\n')