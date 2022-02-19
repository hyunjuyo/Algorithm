from collections import deque

def bfs(start):
    tmp_table = [v[:] for v in table] # table 복사본 생성
    q = deque([start])

    while q:
        point = q.popleft()
        visited[point] += 1
        for p in info[point]:
            visited[p] += 1
            for p2 in info[p]:
                info[point].append(p2)



N = int(input())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

# for v in table:
#     print(v)

info = [[] for _ in range(N)]

for i1, row in enumerate(table):
    for i2, v in enumerate(row):
        if v == 1:
            info[i1].append(i2)

# print(info) # test

visited = [0] * N

bfs(0)