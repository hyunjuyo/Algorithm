

N = int(input())
# arr = []
max_day = 0
info = [list() for _ in range(N+1)]
for _ in range(N):
    D, W = map(int, input().split())
    info[D].append(W)
    max_day = max(max_day, D)
    # arr.append((D, W))

# arr.sort(key=lambda x:(x[0], -x[1]))
# print(arr)

# arr.sort(key=lambda x:(-x[1], x[0]))
# print(arr)

print(info)

result = []
count = 0
tmp = []
for d in range(1, max_day+1):
    # count += len(info[d])
    tmp.extend(info[d])
    if len(tmp) > d:
        tmp.sort(reverse=True)
        result.extend(tmp[:d])
        # count = d
        tmp = [-1] * d

tmp.sort(reverse=True)
for v in tmp:
    if v > 0:
        result.append(v)

print(result) # test
print(sum(result))