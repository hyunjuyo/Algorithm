str_a = input()
str_b = input()

lth_a = len(str_a)
lth_b = len(str_b)

info = [[0] * (lth_a+1) for _ in range(lth_b+1)]

for i in range(1, lth_b+1):
    for j in range(1, lth_a+1):
        if str_b[i-1] == str_a[j-1]: # 알파벳 일치한 경우
            info[i][j] = info[i-1][j-1] + 1
        else:
            info[i][j] = max(info[i-1][j], info[i][j-1])

# for v in info: # test
#     print(v)

print(info[i][j])