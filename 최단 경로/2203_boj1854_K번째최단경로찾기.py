import sys
import heapq

def dijkstra(s):
    h = []
    heapq.heappush(h, (0, s))
    while h:
        ptime, now = heapq.heappop(h)
        if ptime > time_list[now][K-1]:
            continue
        for next, time in info[now]:
            ntime = ptime + time
            if ntime < time_list[next][K-1]:
                time_list[next][K-1] = ntime
                time_list[next].sort()
                heapq.heappush(h, (ntime, next))

N, M, K = map(int, input().split())

info = [list() for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    info[a].append((b, c))

print('info :', info) # test

result = [list() for _ in range(N+1)]
time_list = [[int(1e9)] * K for _ in range(N+1)]
time_list[1][0] = 0
dijkstra(1)

print('time_list', '-'*70) # test
for v in time_list: # test
    print(v)

for row in time_list[1:]:
    if row[K-1] == int(1e9): # K번째 최단경로 존재하지 않는 경우
        print(-1)
    else:
        print(row[K-1])