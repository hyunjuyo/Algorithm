import sys

# 주어진 size 기준의 블루레이 개수 정보 반환 함수
def get_m_count(size_num):
    print(size_num) # test
    m_count = 1 # 블루레이 개수 체크 변수
    tmp_sum = 0 # 1개의 블루레이에 들어갈 크기 체크 변수
    tmp = [] # test
    for i, v in enumerate(lecture):
        tmp_sum += v
        tmp.append(v) # test
        if tmp_sum > size_num:
            t = tmp.pop() # test
            tmp.append('/') # test
            tmp.append(t) # test
            m_count += 1
            tmp_sum = v # 초과된 시점의 v값으로 초기화
    print(m_count, tmp) # test
    print('-'*50) # test

    return m_count

N, M = map(int, input().split())
lecture = list(map(int, sys.stdin.readline().split()))

size_right = sum(lecture) # 가능한 최대값
size_left = max(lecture) # 가능한 최소값
max_num = size_left # 기준 정보 담아두기

# size_left를 증가시켜가며 반복 체크
while True:
    m_count = get_m_count(size_left) # 블루레이 개수 정보 저장
    if m_count > M: # 조건 만족하지 않은 경우
        size_left = (size_left + size_right) // 2 # 증가시키기
    else: # 조건 만족하는 경우
        break

# size_left를 1씩 감소시키며 조건을 만족하는 최소값 정보 출력
while True:
    m_count = get_m_count(size_left)
    if m_count <= M: # 조건 만족하는 경우
        if size_left == max_num: # 가능한 최소값인 경우
            break
        size_left -= 1
    else: # 조건 만족하지 않은 경우
        size_left += 1 # 이전 상태로 복원
        break

print(size_left)