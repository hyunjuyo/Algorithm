import sys
import heapq

INF = sys.maxsize

def dijkstra(s):
    global flag
    h = []
    heapq.heappush(h, (0, s))
    while h:
        t, now = heapq.heappop(h)
        if t > time[now]:
            continue
        for next, dt in info[now]:
            nt = t + dt
            if nt < time[next]:
                time[next] = nt
                heapq.heappush(h, (nt, next))
                count[next] += 1

        for v in count[1:]:
            if v > 6000:
                flag = False
                break
        if flag is False:
            break

N, M = map(int, input().split())

info = [list() for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    info[a].append((b, c))

time = [INF] * (N+1)
count = [0] * (N+1)
flag = True
dijkstra(1)

if flag:
    for v in time[2:]:
        if v == INF:
            print(-1)
        else:
            print(v)
else:
    print(-1)