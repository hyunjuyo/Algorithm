import sys
import heapq

def dijkstra(s):
    h = []
    time_list[s][s] = 0
    heapq.heappush(h, (0, s))
    while h:
        ptime, now = heapq.heappop(h)
        if ptime > time_list[s][now]:
            continue
        for next, time in info[now]:
            ntime = ptime + time
            if ntime < time_list[s][next]:
                time_list[s][next] = ntime
                heapq.heappush(h, (ntime, next))
                conn_list[next][s] = now

N, M = map(int, input().split())

info = [list() for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    info[a].append([b, t])
    info[b].append([a, t])

# print(info) # test

time_list = [[int(1e9)] * (N+1) for _ in range(N+1)]
conn_list = [['-'] * (N+1) for _ in range(N+1)]
for start in range(1, N+1):
    dijkstra(start)

# for v in time_list: # test
#     print(v)
# for v in conn_list: # test
#     print(v)

for v in conn_list[1:]:
    print(*v[1:])