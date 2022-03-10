import sys
import heapq

def dijkstra(num):
    check[num] = True
    time[num] = 0
    h = []
    heapq.heappush(h, (0, num))
    while h:
        pcost, now = heapq.heappop(h)
        if pcost > time[now]:
            continue
        for cost, next in info[now]:
            ncost = pcost + cost
            if time[next] > ncost:
                time[next] = ncost
                heapq.heappush(h, (ncost, next))
                check[next] = True

T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())
    info = [list() for _ in range(N+1)]
    for _ in range(D):
        A, B, S = map(int, sys.stdin.readline().split())
        info[B].append((S, A))
    
    check = [False] * (N+1)
    time = [1e9] * (N+1)
    dijkstra(C)

    print('check :', check) # test
    print('time :', time) # test

    result_count = 0
    result_time = 0
    for i in range(N+1):
        if check[i] == True:
            result_count += 1
            if result_time < time[i]:
                result_time = time[i]

    print(result_count, result_time)