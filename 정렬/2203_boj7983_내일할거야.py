import sys

N = int(input())
arr = []
for _ in range(N):
    D, T = map(int, sys.stdin.readline().split())
    arr.append((D, T))

arr.sort(key=lambda x:(x[1], x[0]))

d, t = arr.pop()
start = t - (d - 1)
flag_day = start - 1
while arr:
    d, t = arr.pop() # 기한이 가장 늦고, 오래 걸리는 과제 순서로 검토
    print(f'd : {d}, t : {t}, flag_day : {flag_day}') # test
    if flag_day < t:
        start = flag_day - (d - 1)
    else:
        start = t - (d - 1)
    flag_day = start - 1

    print(start) # test

print(flag_day)