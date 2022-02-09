# ----------------------------------------
# # 구현 아이디어
# 1. 
# ----------------------------------------

def rotate_90(table):
    tmp_table = [[0] * N for _ in range(N)] # 0으로 초기화

    for i in range(N):
        for j in range(N):
            tmp_table[i][j] = table[N-1-j][i]

    return tmp_table

# 이동 및 병합 함수 정의
def move_n_merge(table, dir):

    # dir값에 따라 테이블 회전시키기
    if dir == 0: # up => 현상태 유지
        tmp_table = [table[row][:] for row in range(N)]
    elif dir == 1: # right => +270도
        tmp_table = rotate_90(table)
        tmp_table = rotate_90(tmp_table)
        tmp_table = rotate_90(tmp_table)
    elif dir == 2: # down => +180도
        tmp_table = rotate_90(table)
        tmp_table = rotate_90(tmp_table)
    else: # left => +90도
        tmp_table = rotate_90(table)
        
    # index 이동 방향 => 회전된 테이블 기준 위쪽
    dir_x = 0
    dir_y = -1

    for i in range(N):
        for j in range(N):
            if tmp_table[i][j] == 0: # 블록이 아닌 경우
                continue
            # 현재 좌표
            px = j
            py = i
            # 한 칸 이동
            nx = px + dir_x
            ny = py + dir_y
            if nx < 0 or nx >= N or ny < 0 or ny >= N: # 범위를 벗어난 경우
                continue

            # 블록이 없는 경우 계속 이동
            while nx >= 0 and nx < N and ny >= 0 and ny < N and tmp_table[ny][nx] == 0:
                nx += dir_x
                ny += dir_y

            if nx < 0 or nx >= N or ny < 0 or ny >= N: # 범위의 끝까지 도달한 경우
                nx -= dir_x
                ny -= dir_y
                tmp_table[ny][nx] = tmp_table[py][px]
                tmp_table[py][px] = 0
            elif tmp_table[ny][nx] == tmp_table[py][px]: # 블록을 만났는데 값이 같은 경우
                tmp_table[ny][nx] += tmp_table[py][px]
                tmp_table[py][px] = 0
            else: # 블록을 만났는데 값이 다른 경우
                if ny == py - 1: # 이미 붙어있어 이동이 없는 경우
                    continue
                else: # 이동이 있는 경우
                    nx -= dir_x
                    ny -= dir_y
                    tmp_table[ny][nx] = tmp_table[py][px]
                    tmp_table[py][px] = 0

    # 회전된 테이블 원복
    if dir == 0: # up => 현상태 유지
        pass
    elif dir == 1: # right => +90도
        tmp_table = rotate_90(tmp_table)
    elif dir == 2: # down => +180도
        tmp_table = rotate_90(tmp_table)
        tmp_table = rotate_90(tmp_table)
    else: # left => +270도
        tmp_table = rotate_90(tmp_table)
        tmp_table = rotate_90(tmp_table)
        tmp_table = rotate_90(tmp_table)

    return tmp_table

N = int(input())

# 입력값 기준 table 저장
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))        

for row in table: # test
    print(row)
print('-'*30)

tmp_table = move_n_merge(table, 0)

for row in tmp_table:
    print(row)