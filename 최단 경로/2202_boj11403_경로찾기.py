import sys
sys.setrecursionlimit(100000)

def dfs(now, start):
    visited[start] = 1

    for p in info[start]:
        table[now][p] = 1
        if visited[p] == 0:
            dfs(now, p)

N = int(input())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

info = [[] for _ in range(N)]

for i1, row in enumerate(table):
    for i2, v in enumerate(row):
        if v == 1:
            info[i1].append(i2)

# print(info) # test

for idx in range(N):
    visited = [0] * N
    dfs(idx, idx)

# for v in table: # test
#     print(v)

for v in table:
    print(' '.join(map(str, v)))