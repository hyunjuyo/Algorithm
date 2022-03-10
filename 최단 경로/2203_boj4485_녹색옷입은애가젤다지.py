import sys
import heapq

def dijkstra(pos):
    cost_list[pos[0]][pos[1]] = table[pos[0]][pos[1]]
    h = []
    heapq.heappush(h, (table[0][0], pos))
    while h:
        pcost, now = heapq.heappop(h)
        if pcost > cost_list[now[0]][now[1]]:
            continue
        for c, p in info[now[0]][now[1]]:
            ncost = pcost + c
            if ncost < cost_list[p[0]][p[1]]:
                cost_list[p[0]][p[1]] = ncost
                heapq.heappush(h, (ncost, p))
        # for v in cost_list: # test
        #     print(v)
        # print('-'*30) # test

p_num = 1
while True:
    N = int(input())
    if N == 0:
        break
    table = []
    for _ in range(N):
        table.append(list(map(int, sys.stdin.readline().split())))

    # 연결된 cost, 위치 정보 담기
    info = [[list() for _ in range(N)] for _ in range(N)]
    # for v in info: # test
    #     print([id(v2) for v2 in v])
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny = y + dir[i][0]
                nx = x + dir[i][1]
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue
                info[y][x].append((table[ny][nx], (ny, nx))) # 연결된 (cost, 위치) 정보 추가
    # for v in info: # test
    #     print(v)


    cost_list = [[int(1e9)] * N for _ in range(N)]
    dijkstra((0, 0))
    print(f'Problem {p_num}:', cost_list[N-1][N-1]) # 결과 출력
    p_num += 1