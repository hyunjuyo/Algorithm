from collections import deque

# 모든 토마토가 익어있는 상태인지 체크하는 함수
def is_complete(table):
    for i in range(N):
        for j in range(M):
            for h in range(H):
                if table[i][j][h] == 0: # 익지 않은 토마토 있을 경우
                    return False
    return True

def bfs(tomato_list):
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
                next_tomato_list.append((ny, nx, nh))

    return next_tomato_list

M, N, H = map(int, input().split())
table = [[list() for _ in range(M)] for _ in range(N)] # 3차원 배열 초기화

# for row in table: # test
#     print(row)
# for row in table: # test
#     print(list(map(id, row)))

# 층별 정보 table 저장
tomato_list = [] # 익은 토마토 위치 정보 저장
for h in range(H):
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(M):
            table[i][j].append(tmp[j])
            if tmp[j] == 1:
                tomato_list.append((i, j, h))

# for row in table: # test
#     print(row)

dir = [(-1, 0 ,0), (0, 1, 0), (1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)] # 북, 동, 남, 서, 위, 아래

day = 0
while not(is_complete(table)) and tomato_list:
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

if is_complete(table):
    print(day)
else:
    print(-1)