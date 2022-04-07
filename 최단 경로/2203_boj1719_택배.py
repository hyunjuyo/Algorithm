import sys
import heapq

def dijkstra(s):
    h = []
    heapq.heappush(h, (0, s))
    while h:
        time, now = heapq.heappop(h)
        if time 


N, M = map(int, input().split())

info = [list() for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    info[a].append((b, t))
    info[b].append((a, t))

print(info)

time_list = [int(1e9)] * (N+1)
dijkstra(1)