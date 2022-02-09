# ----------------------------------------
# # 구현 아이디어
# 1. 
# ----------------------------------------

class BlockNumber:
    def __init__(self, num):
        self.value = num
        self.flag = 0

def rotate_90(table):
    # tmp_table 생성 및 초기화
    tmp_table = []
    for _ in range(N):
        tmp = []
        for _ in range(N):
            tmp.append(BlockNumber(0)) # 0으로 초기화
        tmp_table.append(tmp)

    # 90도 회전
    for i in range(N):
        for j in range(N):
            tmp_table[i][j].value = table[N-1-j][i].value

    return tmp_table

# 이동 및 병합 함수 정의
def move_n_merge(table, dir):

    # dir값에 따라 테이블 회전시키기
    if dir == 'up': # up => 현상태 유지
        tmp_table = [table[row][:] for row in range(N)]
    elif dir == 'right': # right => +270도
        tmp_table = rotate_90(table)
        tmp_table = rotate_90(tmp_table)
        tmp_table = rotate_90(tmp_table)
    elif dir == 'down': # down => +180도
        tmp_table = rotate_90(table)
        tmp_table = rotate_90(tmp_table)
    else: # left => +90도
        tmp_table = rotate_90(table)
        
    # index 이동 방향 => 회전된 테이블 기준 위쪽
    dir_x = 0
    dir_y = -1

    for i in range(N):
        for j in range(N):
            if tmp_table[i][j].value == 0: # 블록이 아닌 경우
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
            while nx >= 0 and nx < N and ny >= 0 and ny < N and tmp_table[ny][nx].value == 0:
                nx += dir_x
                ny += dir_y

            if nx < 0 or nx >= N or ny < 0 or ny >= N: # 범위의 끝까지 도달한 경우
                nx -= dir_x
                ny -= dir_y
                tmp_table[ny][nx].value = tmp_table[py][px].value
                tmp_table[py][px].value = 0
            elif tmp_table[ny][nx].value == tmp_table[py][px].value: # 블록을 만났는데 값이 같은 경우
                if tmp_table[ny][nx].flag == 0: # 병합된 블록이 아닌 경우
                    tmp_table[ny][nx].value += tmp_table[py][px].value
                    tmp_table[ny][nx].flag = 1 # flag 변경
                    tmp_table[py][px].value = 0
                else: # 이미 병합된 블록인 경우
                    nx -= dir_x
                    ny -= dir_y
                    tmp_table[ny][nx].value = tmp_table[py][px].value
                    tmp_table[py][px].value = 0
            else: # 블록을 만났는데 값이 다른 경우
                if ny == py - 1: # 이미 붙어있어 이동이 없는 경우
                    continue
                else: # 이동이 있는 경우
                    nx -= dir_x
                    ny -= dir_y
                    tmp_table[ny][nx].value = tmp_table[py][px].value
                    tmp_table[py][px].value = 0

    # 회전된 테이블 원복
    if dir == 'up': # up => 현상태 유지
        pass
    elif dir == 'right': # right => +90도
        tmp_table = rotate_90(tmp_table)
    elif dir == 'down': # down => +180도
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
    tmp = []
    for num in list(map(int, input().split())):
        tmp.append(BlockNumber(num))
    table.append(tmp)

# for row in table: # test
#     for v in row:
#         print(v.value, end=' ')
#     print()
# print('-'*30)

tmp_table = [table[row][:] for row in range(N)]

dir_order = ['right', 'up', 'up', 'right', 'right']
dir_order2 = ['up', 'left', 'up', 'right', 'right']
dir_order3 = ['right', 'up', 'up', 'right', 'right']

for dir in dir_order2:
    print('-'*30)
    print(dir)
    tmp_table = move_n_merge(tmp_table, dir)

    for row in tmp_table: # test
        for v in row:
            print(v.value, end=' ')
        print()