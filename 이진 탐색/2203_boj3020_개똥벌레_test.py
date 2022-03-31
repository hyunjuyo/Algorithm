import sys

def draw_wall(i, h):
    if i % 2 == 0:
        start = H-1
        for _ in range(h):
            info[start] += 1
            # table[start][i] = 1 # test
            start -= 1
    else:
        start = 0
        for _ in range(h):
            info[start] += 1
            # table[start][i] = 1 # test
            start += 1

N, H = map(int, input().split())
info = [0] * H
# table = [[0] * N for _ in range(H)] # test
for i in range(N):
    h = int(sys.stdin.readline())
    draw_wall(i, h)

info.sort()
min_num = info[0]

count = N + 1
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