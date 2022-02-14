import sys

# 주어진 size 기준의 블루레이 개수 정보 반환 함수
def get_m_count(size_num):
    m_count = 1 # 블루레이 개수 체크 변수
    tmp_sum = 0 # 1개의 블루레이에 들어갈 크기 체크 변수
    for v in lecture:
        tmp_sum += v
        if tmp_sum > size_num:
            m_count += 1
            tmp_sum = v # 초과된 시점의 v값으로 초기화

    return m_count

N, M = map(int, input().split())
lecture = list(map(int, sys.stdin.readline().split()))

size_num = sum(lecture) # 가장 큰 값으로 초기화

# size_num 반으로 줄이며 반복 체크
while True:
    m_count = get_m_count(size_num) # 블루레이 개수 정보 저장
    if m_count <= M:
        size_num = size_num // 2
    else:
        break

# size_num 최소값 제한
max_lecture = max(lecture)
if size_num < max_lecture:
    size_num = max_lecture

# size_num 1씩 증가시키며 최초로 가능해지는 시점 size_num 출력
while True:
    m_count = get_m_count(size_num)
    if m_count > M:
        size_num += 1
    else:
        break

print(size_num)