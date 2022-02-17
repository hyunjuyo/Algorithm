import sys

N, K = map(int, input().split())

info = [[0] * (K+1) for _ in range(N+1)]

max_num = 0
for i in range(1, N+1):
    W, V = map(int, sys.stdin.readline().split())

    for j in range(1, K+1):
        if W <= j:
            info[i][j] = max(info[i-1][j], info[i-1][j-W] + V) # 최대값 기준 저장
            if info[i][j] > max_num:
                max_num = info[i][j]
        else:
            info[i][j] = info[i-1][j]

# for v in info: # test
#     print(v)

print(max_num)