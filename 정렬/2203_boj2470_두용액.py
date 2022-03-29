from collections import deque, defaultdict

N = int(input())
arr = list(map(int, input().split()))

l = []
r = []
for v in arr:
    if v < 0:
        l.append(v)
    else:
        r.append(v)

l.sort()
r.sort(reverse=True)

l.append(0)
r.append(0)

# print(l) # test
# print(r) # test

min_num = 2 * 10**9
min_dict = defaultdict(list)
l = deque(l)
r = deque(r)
lv = l.popleft()
rv = r.popleft()
while lv and rv:
    # print('lv, rv :', lv, rv, '=>', lv + rv) # test
    if abs(lv + rv) < min_num:
        min_num = abs(lv + rv)
        min_dict[min_num].append((lv, rv))
        # print(min_dict) # test
    if lv == 0 and rv == 0:
        break
    elif lv + rv == 0:
        break
    elif lv + rv > 0:
        rv = r.popleft()
    else:
        lv = l.popleft()

if lv == 0:
    r.pop() # 0 없애기
    # print('r:', r) # test
    if len(r) >= 2:
        tmp = abs(r[-1] + r[-2])
        if tmp < min_num:
            min_dict[tmp].append((r[-1], r[-2]))
    elif len(r) >= 1:
        tmp = abs(r[-1] + rv)
        if tmp < min_num:
            min_dict[tmp].append((r[-1], rv))
elif rv == 0 and len(l) >= 2:
    l.pop() # 0 없애기
    # print('l:', l) # test
    if len(l) >= 2:
        tmp = abs(l[-1] + l[-2])
        if tmp < min_num:
            min_dict[tmp].append((l[-1], l[-2]))
    elif len(l) >= 1:
        tmp = abs(l[-1] + lv)
        if tmp < min_num:
            min_dict[tmp].append((l[-1], lv))

print('result :', min_dict) # test
print(*sorted(list(min_dict[min(min_dict.keys())][0])))