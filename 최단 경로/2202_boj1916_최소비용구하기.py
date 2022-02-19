import sys
import heapq

def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    cost_list[start] = 0
    while heap_data:
        pcost, now = heapq.heappop(heap_data)
        if cost_list[now] < pcost:
            continue
        for v in info[now]:
            ncost = pcost + v[1]
            if cost_list[v[0]] > ncost:
                cost_list[v[0]] = ncost
                heapq.heappush(heap_data, (ncost, v[0]))

N = int(input())
info = [[] for _ in range(N+1)]

M = int(input())
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    info[a].append((b, cost))

start, end = map(int, input().split())
cost_list = [1e9] * (N+1)
dijkstra(start)

# print(cost_list) # test
print(cost_list[end])