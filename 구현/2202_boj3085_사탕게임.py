# 한 줄에서 가장 긴 연속 부분 측정 함수(line 내 스왑 X)
def get_one_line_max_num(one_line):
    lth_list = []
    lth = 1
    for i in range(N):
        if i == 0:
            continue
        if one_line[i-1] == one_line[i]:
            lth += 1
        else:
            lth_list.append(lth)
            lth = 1
    lth_list.append(lth)
    # print('lth_list :', lth_list) # test
    return max(lth_list)

# 두 줄에서 가장 긴 연속 부분 측정 함수(line간 스왑 O, line 내 스왑 X)
def get_two_line_max_num(two_line):
    # 현 상태에서의 가장 긴 연속 부분 측정
    num1 = get_one_line_max_num(two_line[0])
    num2 = get_one_line_max_num(two_line[1])
    max_num = max(num1, num2)
    
    # 케이스별 위치 바꾼 뒤 가장 긴 연속 부분 측정
    for case in range(N):
        tmp_0 = two_line[0][:] # 복사본 생성
        tmp_1 = two_line[1][:] # 복사본 생성
        tmp_0[case], tmp_1[case] = tmp_1[case], tmp_0[case] # 해당 위치 swap
        num1 = get_one_line_max_num(tmp_0)
        num2 = get_one_line_max_num(tmp_1)
        if max_num < max(num1, num2):
            max_num = max(num1, num2)

    return max_num

def get_rotate_90(table):
    table_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            table_90[i][j] = table[N-j-1][i]

    return table_90

N = int(input())
table = []
for _ in range(N):
    table.append(list(input()))

# 두 줄씩 추출해 가장 긴 연속 부분 측정(line간 스왑 O, line 내 스왑 X)
total_max_num = 0
# 행 방향 탐색
for idx in range(N-1):
    two_line = [table[i][:] for i in range(idx, idx+2)] # 두 줄 복사본 생성
    max_num = get_two_line_max_num(two_line)
    if total_max_num < max_num:
        total_max_num = max_num
# 열 방향 탐색
table_90 = get_rotate_90(table)
for idx in range(N-1):
    two_line = [table_90[i][:] for i in range(idx, idx+2)] # 두 줄 복사본 생성
    max_num = get_two_line_max_num(two_line)
    if total_max_num < max_num:
        total_max_num = max_num

# 한 줄씩 추출해 가장 긴 연속 부분 측정(line 내 스왑 O)
# 행 방향 탐색
for i in range(N):
    for j in range(N-1):
        one_line = table[i][:] # 복사본 생성
        one_line[j], one_line[j+1] = one_line[j+1], one_line[j] # swap
        max_num = get_one_line_max_num(one_line)
        if total_max_num < max_num:
            total_max_num = max_num
# 열 방향 탐색
for i in range(N):
    for j in range(N-1):
        one_line = table_90[i][:] # 복사본 생성
        one_line[j], one_line[j+1] = one_line[j+1], one_line[j] # swap
        max_num = get_one_line_max_num(one_line)
        if total_max_num < max_num:
            total_max_num = max_num

print(total_max_num)