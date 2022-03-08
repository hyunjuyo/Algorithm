import sys

N = int(input())
NUM = list(map(int, input().split()))
M = int(input())

table = [[-1] * (N+1) for _ in range(N+1)]

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())

    if S == E:
        table[S][E] = 1
        print(1)    
    elif table[S+1][E-1] == 1:
        if NUM[S-1] == NUM[E-1]:
            table[S][E] = 1
            print(1)
        else:
            print(0)
    elif table[S+1][E-1] == 0:
        table[S][E] = 0
        print(0)
    else:
        num = NUM[S-1:E]
        if num == num[::-1]:
            table[S][E] = 1
            print(1)
        else:
            table[S][E] = 0
            print(0)