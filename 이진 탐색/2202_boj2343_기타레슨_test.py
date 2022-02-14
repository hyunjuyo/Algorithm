N, M = map(int, input().split())
lecture = list(map(int, input().split()))

size_num = sum(lecture) # 가장 큰 값으로 초기화

# size_num 반으로 줄이며 반복 체크
while True:
    print(size_num) # test
    m_count = 1 # 블루레이 개수 체크 변수
    tmp_sum = 0 # 1개의 블루레이에 들어갈 크기 체크 변수
    for v in lecture:
        tmp_sum += v
        if tmp_sum > size_num:
            m_count += 1
            tmp_sum = v # 초과된 시점의 강의 길이로 초기화
    if m_count <= M:
        size_num = size_num // 2
    else:
        break

# size_num 최소값 제한
max_lecture = max(lecture)
if size_num < max_lecture:
    size_num = max_lecture

# size_num 1씩 증가시키며 최초로 가능해지는 시점 정보 출력
while True:
    print(size_num) # test
    m_count = 1
    tmp_sum = 0
    tmp = [] # test
    for i, v in enumerate(lecture):
        tmp_sum += v
        tmp.append(v) # test
        if tmp_sum > size_num:
            t = tmp.pop() # test
            tmp.append('/') # test
            tmp.append(t) # test
            m_count += 1
            tmp_sum = v
    print(m_count, tmp) # test
    print('-'*50) # test
    if m_count > M:
        size_num += 1
    else:
        break

print(size_num)