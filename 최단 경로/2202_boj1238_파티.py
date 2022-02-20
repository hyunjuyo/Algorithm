import sys
import heapq

def dijkstra(point):
    heap_list = []

    heapq.heappush(heap_list, (0, point))
    while heap_list:
        pcost, now = heapq.heappop(heap_list)
        if cost_list[now] < pcost:
            continue
        for v in info[now]:
            ncost = pcost + v[1]
            if cost_list[v[0]] > ncost:
                cost_list[v[0]] = ncost
                heapq.heappush(heap_list, (ncost, v[0]))


N, M, X = map(int, input().split())
info = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    info[a].append((b, cost))

# print(info) # test

result = [0] * (N+1)

for n in range(1, N+1):
    if n == X: # n과 X가 같은 경우 조건 추가 !!!!! 
        result[n] = 0
        continue

    # print('-'*30) # test
    cost_list = [1e9] * (N+1)
    dijkstra(n) # n에서 출발한 경우 시간 정보 저장
    # print(f'{n}->{X}', cost_list, cost_list[X]) # test
    time1 = cost_list[X]
    cost_list = [1e9] * (N+1)
    dijkstra(X) # X에서 출발한 경우 시간 정보 저장
    # print(f'{X}->{n}', cost_list, cost_list[n]) # test
    time2 = cost_list[n]

    result[n] = time1 + time2 # n에서 X로 이동한 시간 + X에서 n으로 이동한 시간
    # print('-'*30) # test

# print(result) # test
print(max(result))