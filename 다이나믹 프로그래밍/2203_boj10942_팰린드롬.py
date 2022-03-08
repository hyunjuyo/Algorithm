import sys

N = int(input())
NUM = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    num = NUM[S-1:E]
    if num == num[::-1]:
        print(1)
    else:
        print(0)