import sys

N = int(input())

arr = []
for _ in range(N):
    arr.append(tuple(map(int, sys.stdin.readline().split())))

arr_s = sorted(arr, key=lambda x : (x[1], x[0]))

count = 1
end_time = arr_s[0][1]
for i, v in enumerate(arr_s):
    if i == 0 or v[0] < end_time:
        continue
    else:
        count += 1
        end_time = v[1]

print(count)