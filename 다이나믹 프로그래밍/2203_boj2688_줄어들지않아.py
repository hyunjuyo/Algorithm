T = int(input())
output = []
for _ in range(T):
    n = int(input())
    output.append(n)

result = [0] * 65
info = [list() for _ in range(65)]
result[1] = 10

# 2자리
for n in range(10, 0, -1):
    info[2].append(n)
for v in info[2]:
    result[2] += v

# 3~64자리
for n in range(3, 65):
    start = result[n-1]
    info[n].append(start)
    for i, v in enumerate(info[n-1]):
        if i == 9:
            break
        start -= v
        info[n].append(start)
    for v in info[n]:
        result[n] += v

print(info) # test
print(result) # test

for n in output:
    print(result[n])