import sys
import heapq
from collections import deque

# 특정 무게로 도달 가능여부 판단
def bfs(s, e, cand):
    q = deque([s])
    while q:
        now = q.popleft()
        visited[now] = True
        if visited[e] is True:
            return True
        while info[now]:
            limit, next = heapq.heappop(info[now])
            print('limit, next :', limit, next) # test
            if visited[next] is False and cand <= -limit:
                q.append(next)
    return False

N, M = map(int, input().split())

info_org = [list() for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(info_org[a], (-c, b))
    heapq.heappush(info_org[b], (-c, a))

s, e = map(int, input().split())

result = 0
l = 1
r = 10**9
while l <= r:
    mid = (l+r) // 2
    print('mid :', mid) # test
    visited = [False] * (N+1)
    info = [row[:] for row in info_org] # deepcopy로 하면 시간초과!!!!!
    print(info) # test
    if bfs(s, e, mid) == True:
        l = mid + 1
        result = max(result, mid)
    else:
        r = mid - 1

print(result)