import copy
import sys

N = int(input())

table = []
for i in range(N):
    table.append(list(sys.stdin.readline()))

min_count = N * N # 가능한 최대값으로 초기화

for bit in range(1 << N): # 행에 대한 경우의수 모두 체크
    tmp_table = copy.deepcopy(table)
    for i in range(N):
        if bit & (1 << i): # 해당 행 판단
            # print(i) # test
            for j in range(N): # 해당 행 모두 뒤집기
                if tmp_table[i][j] == 'H':
                    tmp_table[i][j] = 'T'
                else:
                    tmp_table[i][j] = 'H'
    
    # for row in tmp_table: # test
    #     print(row)
    # print('-'*30) # test
    
    # 열별로 'T'의 최소 개수 확인(뒤집는 경우 고려)
    total_count = 0
    for j in range(N):
        count = 0
        for i in range(N):
            if tmp_table[i][j] == 'T':
                count += 1
        total_count += min(count, N - count) # 뒤집는 경우 고려
    
    # 모든 경우의수와 비교
    if total_count < min_count:
        min_count = total_count

print(min_count)