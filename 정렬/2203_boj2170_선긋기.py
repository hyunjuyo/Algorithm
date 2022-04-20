import sys

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

arr.sort()

lines = []
l = arr[0][0]
r = arr[0][1]
lines.append([l, r])
for v in arr[1:]:
    if v[0] <= r:
        if r < v[1]:
            r = v[1] # 연결된 선 범위 업데이트
            lines[-1][1] = v[1]
    else:
        l = v[0]
        r = v[1]
        lines.append([l, r])
    print(lines) # test

result = 0
for v in lines:
    result += (v[1] - v[0])

print(result)