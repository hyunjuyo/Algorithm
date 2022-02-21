from collections import deque

def bfs(point):
    visited[point] = True
    q = deque([point])
    while q:
        p = q.popleft()
        for v in info[p]:
            if visited[v] == False:
                visited[v] = True
                q.append(v)

N = int(input())
info = [[] for _ in range(N+1)]

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    info[a].append(b)
    info[b].append(a)

visited = [False] * (N+1)
bfs(1)

# print(visited) # test
print(sum(visited) - 1)