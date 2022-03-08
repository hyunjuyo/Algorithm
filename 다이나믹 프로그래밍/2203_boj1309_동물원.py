N = int(input())

arr = [[0] * 3 for _ in range(N+1)]
for i in range(1, N+1):
    if i == 1:
        arr[i][0] = 1 # 현재 라인에 사자를 넣지 않는 경우
        arr[i][1] = 1 # 현재 라인 왼쪽칸에 사자를 넣는 경우
        arr[i][2] = 1 # 현재 라인 오른쪽칸에 사자를 넣는 경우
        continue
    arr[i][0] = (arr[i-1][0] + arr[i-1][1] + arr[i-1][2]) % 9901
    arr[i][1] = (arr[i-1][0] + arr[i-1][2]) % 9901
    arr[i][2] = (arr[i-1][0] + arr[i-1][1]) % 9901

for v in arr: # test
    print(v)

print(sum(arr[-1]) % 9901)