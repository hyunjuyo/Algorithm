def action(y, x, d):
    global count

    table[y][x] = 2 # 청소 완료
    dir_left = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    dir_back = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    flag = 4
    while True:
        ny = y + dir_left[d][0]
        nx = x + dir_left[d][1]
        # print(f'[left] ({y}, {x}) -> ({ny}, {nx})') # test
        if table[ny][nx] == 0: # 청소하지 않은 공간이 있을 경우
            d = (d + 3) % 4 # 해당 방향으로 회전
            y = ny
            x = nx
            table[y][x] = 2 # 청소 완료
            count += 1 # 청소한 칸 개수 +1
            flag = 4 # 네 방향 체크 flag 초기화
            # # 청소 과정 시각화(test)
            # for i in range(N): # test
            #     for j in range(M):
            #         if i == y and j == x:
            #             print('\033[30m\033[43m' + str(table[i][j]) + '\033[0m', end=' ')
            #         else:
            #             print(table[i][j], end=' ')
            #     print()
            continue
        else:
            flag -= 1 # 4 방향 체크
            d = (d + 3) % 4 # 해당 방향으로 회전
        
        if flag == 0:
            ny = y + dir_back[d][0]
            nx = x + dir_back[d][1]
            # print(f'[back] ({y}, {x}) -> ({ny}, {nx})') # test
            if table[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx
                flag = 4
            continue

N, M = map(int, input().split())
r, c, d = map(int, input().split())

table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

count = 1
action(r, c, d)

print(count)