import sys

def get_max_count(score_list):
    count = 0
    score_list.sort()

    tmp_min = 100001 # 조건 중 가장 큰 수로 초기화
    for i, (a, b) in enumerate(score_list):
        print(f'(a, b) => ({a}, {b}) / tmp_min => {tmp_min}')
        if tmp_min > b:
            count += 1
            print("here~!!")
        if tmp_min > b: # 가장 높은 순위 저장 => min() 사용 시 시간초과 !!!!!
            tmp_min = b

    return count


T = int(input())

# case 딕셔너리에 정보 저장
case = {}
for i in range(T):
    case[i] = []
    N = int(input())
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        case[i].append((a, b))

# 케이스별 최대 인원수 측정 및 출력
for i in range(T):
    max_num = get_max_count(case[i])
    print(max_num)