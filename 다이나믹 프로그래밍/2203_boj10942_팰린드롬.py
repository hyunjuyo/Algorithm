import sys

N = int(input())
NUM = list(map(int, input().split()))
M = int(input())

table = [[0] * N for _ in range(N)]

for i in range(N):
    table[i][i] = 1

for i in range(N-1):
    if NUM[i] == NUM[i+1]:
        table[i][i+1] = 1

for lth in range(2, N+1):
    for i in range(N-lth):
        if NUM[i] == NUM[i+lth] and table[i+1][i+lth-1] == 1:
            table[i][i+lth] = 1

for v in table: # test
    print(v)

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(table[S-1][E-1])