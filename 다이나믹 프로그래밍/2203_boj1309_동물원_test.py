N = int(input())

result = [0] * (N+1)
minus = [0] * (N+1)
for i in range(1, N+1):
    if i == 1:
        result[i] = 3
        minus[i] = 2 # 맨 아래줄에 사자가 있는 경우의수
        continue
    elif i == 2:
        result[i] = result[i-1] * 3 - minus[i-1]
        minus[i] = minus[i-1] * 2
        continue

    result[i] = (result[i-1] * 3 - minus[i-1]) % 9901
    minus[i] = minus[i-1] * 2 + 2

print(result)