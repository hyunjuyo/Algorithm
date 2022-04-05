import sys

N = int(input())
table = []
# for _ in range(N):
#     table.append(list(map(int, sys.stdin.readline().split())))

# 결과 저장용
max_num = [[0, 0, 0] for _ in range(2)]
min_num = [[0, 0, 0] for _ in range(2)]

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))

    max_num[1][0] = max(max_num[0][0], max_num[0][1]) + tmp[0]
    min_num[1][0] = min(min_num[0][0], min_num[0][1]) + tmp[0]

    max_num[1][1] = max(max_num[0][0], max_num[0][1], max_num[0][2]) + tmp[1]
    min_num[1][1] = min(min_num[0][0], min_num[0][1], min_num[0][2]) + tmp[1]

    max_num[1][2] = max(max_num[0][1], max_num[0][2]) + tmp[2]
    min_num[1][2] = min(min_num[0][1], min_num[0][2]) + tmp[2]

    max_num[0][0], max_num[0][1], max_num[0][2] = max_num[1][0], max_num[1][1], max_num[1][2]
    min_num[0][0], min_num[0][1], min_num[0][2] = min_num[1][0], min_num[1][1], min_num[1][2]

    print(max_num) # test
    print(min_num) # test

print(max(max_num), min(min_num))