import sys
from collections import deque

# DFS 함수
def dfs(V):
    print(V, end=' ')
    visited[V] = True

    for spot in spot_info[V]:
        if visited[spot] == False:
            dfs(spot)

# BFS 함수
def bfs(V):
    queue = deque([V])

    while queue:
        num = queue.popleft()
        print(num, end=' ')
        visited[num] = True
        for spot in spot_info[num]:
            if visited[spot] == False:
                if spot not in queue:
                    queue.append(spot)

N, M, V = map(int, input().split())

spot_info = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    spot_info[a].append(b)
    spot_info[b].append(a)

# 오름차순 정렬 => 작은 번호 먼저 방문
for spot in spot_info:
    spot.sort()

# DFS 결과 출력
visited = [False] * (N + 1)
dfs(V)

print()

# BFS 결과 출력
visited = [False] * (N + 1)
bfs(V)