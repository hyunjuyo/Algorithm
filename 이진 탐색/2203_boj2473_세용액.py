N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr) # test

result = []
min_num = 10**9 * 3 # 임의의 가장 큰 수
v1, v2, v3 = 0, 0, 0
for i in range(N-2):
    lp = i + 1
    rp = N - 1
    while lp < rp:
        tmp = arr[i] + arr[lp] + arr[rp]
        print(f'{arr[i]}({i}), {arr[lp]}({lp}), {arr[rp]}({rp}) =>', tmp) # test
        if abs(tmp) < min_num:
            min_num = abs(tmp)
            v1, v2, v3 = arr[i], arr[lp], arr[rp]
            print('here~!!') # test
        if tmp > 0:
            rp -= 1
        elif tmp < 0:
            lp += 1
        else:
            break

print(v1, v2, v3)