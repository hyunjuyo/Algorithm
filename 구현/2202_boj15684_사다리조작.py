# ---------------------------------------------------------
# # 구현 방식
# 1. 가로선 입력가능 위치정보 파악 및 저장
# 2. 추가해야 하는 가로선 개수 증가시키며 각 케이스별 사다리게임 결과 확인
# ---------------------------------------------------------

from itertools import combinations

def is_same_result(table, N, H):
    ret = True
    i_arr = [i for i in range(1, N + 1)]

    # i번 세로선의 결과가 i번인지 확인
    for i in i_arr:
        now_i = i
        for j in range(1, H + 1): # 순서대로 가로선 체크 후 위치 조정
            if table[j][now_i] == '-':
                now_i += 1
            elif table[j][now_i - 1] == '-':
                now_i -= 1
        if i != now_i:
            ret = False
            break
    
    return ret

N, M, H = map(int, input().split())

# table 생성 및 '*'로 초기화
table = [['*'] * (N + 1) for _ in range(H + 1)]

# 입력값으로 주어진 가로선 그리기
for _ in range(M):
    a, b = map(int, input().split())
    table[a][b] = '-'

# 가로선 입력 가능여부 표기 및 입력가능 위치정보 저장
cand_list = []
for i in range(H + 1):
    for j in range(N + 1):
        if i == 0 or j == 0 or j == N: # 테두리인 경우 => 0
            table[i][j] = 0
        elif table[i][j-1] == '-' or table[i][j+1] == '-': # 연속하거나 접한 경우 => ' '
            table[i][j] = ' '
        if table[i][j] == '*': # 가로선 입력가능 위치정보 저장
            cand_list.append((i, j))

# 추가해야 하는 가로선 개수 증가시키며 사다리게임 결과 확인
result = -1
for n in range(4): # 0부터 3까지 체크
    comb_list = list(combinations(cand_list, n)) # 추가개수별 조합 추출

    # 추출된 가로선 추가 및 결과 체크
    for comb in comb_list:
        tmp_table = [table[row][:] for row in range(H + 1)] # table 복사
        for com in comb:
            i, j = com
            tmp_table[i][j] = '-' # 해당 위치 가로선 추가

        if is_same_result(tmp_table, N, H): # 사다리게임 결과 확인
            result = n
            break

    if result != -1:
        break

print(result)