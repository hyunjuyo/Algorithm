result = [] # 높이 차이 최대값 저장용

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort() # 오름차순 정렬

    # 커지다가 작아지는 순서로 배치하기
    left = []
    right = []
    for i, v in enumerate(arr):
        if i % 2 == 0: # 짝수 위치
            left.append(v)
        else: # 홀수 위치
            right.append(v)
    left.extend(right[::-1]) # 커지다가 작아지는 순서로 연결

    # 높이 차이 최대값 구하기
    max_num = -1
    for i in range(1, N):
        diff = abs(left[i-1] - left[i])
        if max_num < diff:
            max_num = diff
    
    result.append(max_num)

print(*result, sep='\n')