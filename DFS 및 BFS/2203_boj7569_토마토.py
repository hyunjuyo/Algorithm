from collections import deque

def bfs(tomato_list):
    global zero_to_one # 0->1 토마토 개수 저장
    next_tomato_list = [] # 일단위 tomato_list 저장용

    q = deque(tomato_list)
    while q:
        y, x, h = q.popleft()
        for i in range(6):
            ny = y + dir[i][0]
            nx = x + dir[i][1]
            nh = h + dir[i][2]
            if ny < 0 or ny >= N or nx < 0 or nx >= M or nh < 0 or nh >= H:
                continue
            if table[ny][nx][nh] == 0:
                table[ny][nx][nh] = 1
                zero_to_one += 1
                next_tomato_list.append((ny, nx, nh))

    return next_tomato_list

M, N, H = map(int, input().split())
table = [[list() for _ in range(M)] for _ in range(N)] # 3차원 배열 초기화

# 층별 정보 table 저장
tomato_list = [] # 익은 토마토 위치 저장
zero_org = 0 # 시작 시점에 익지 않은 토마토 개수 저장
for h in range(H):
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(M):
            table[i][j].append(tmp[j])
            if tmp[j] == 1:
                tomato_list.append((i, j, h))
            elif tmp[j] == 0:
                zero_org += 1

dir = [(-1, 0 ,0), (0, 1, 0), (1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)] # 북, 동, 남, 서, 위, 아래

zero_to_one = 0 # 0->1 토마토 개수 저장
day = 0
while (zero_to_one != zero_org) and tomato_list:
    day += 1
    print(f'day {day}', '-'*50) # test
    tomato_list = bfs(tomato_list) # 일단위로 list 업데이트
    # print(tomato_list) # test
    for h in range(H): # test
        print(f'{h+1}충')
        for i in range(N):
            for j in range(M):
                print(table[i][j][h], end=' ')
            print()

if zero_to_one == zero_org:
    print(day)
else:
    print(-1)