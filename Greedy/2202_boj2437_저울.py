N = int(input())
n_list = list(map(int, input().split()))

n_list.sort()

num = 1
for v in n_list:
    if num >= v:
        num += v
    else:
        break

print(num)