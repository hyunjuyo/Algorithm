import sys

N, H = map(int, input().split())
up = [0] * (H + 1)
down = [0] * (H + 1)
for i in range(N):
    h = int(sys.stdin.readline())
    if i % 2 == 0:
        down[h] += 1
    else:
        up[h] += 1

# 누적합 저장
for i in range(H-1, 0, -1):
    up[i] += up[i+1]
    down[i] += down[i+1]

print('up :', up) # test
print('down :', down) # test

info = [0] * (H + 1)
for h in range(1, H+1):
    info[h] = down[h] + up[H-h+1]

print(info) # test

info.pop(0)
info.sort()
min_num = info[0]

count = int(1e9)
l = 0
r = H - 1
while l <= r:
    mid = (l + r) // 2
    if info[mid] > min_num:
        r = mid - 1
        count = min(count, mid)
    else:
        l = mid + 1

print(min_num, count)