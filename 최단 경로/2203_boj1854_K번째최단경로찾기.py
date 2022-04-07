import sys
import heapq

def dijkstra(s, k_num):
    h = []
    heapq.heappush(h, (0, s))
    while h:
        ptime, now = heapq.heappop(h)
        if ptime > time_list[now][k_num]:
            continue
        for next, time in info[now]:
            ntime = ptime + time
            if ntime < time_list[next][k_num]:
                if ntime not in time_list[next][1:k_num]: # 기존 최단경로가 아닌 경우
                    time_list[next][k_num] = ntime
                heapq.heappush(h, (ntime, next))

N, M, K = map(int, input().split())

info = [list() for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    info[a].append((b, c))

print('info :', info) # test

time_list = [[int(1e9)] * (K+1) for _ in range(N+1)]
time_list[1][1] = 0 # 시작지점 1에 대해 첫번째 경우만 0으로 설정
for k_num in range(1, K+1):
    dijkstra(1, k_num)

print('time_list', '-'*70)
for v in time_list[1:]: # test
    print(v[1:])

for row in time_list[1:]:
    if row[K] == int(1e9): # K번째 최단경로 존재하지 않는 경우
        print(-1)
    else:
        print(row[K])