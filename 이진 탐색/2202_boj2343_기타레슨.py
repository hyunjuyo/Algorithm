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
lecture = list(map(int, input().split()))

l = max(lecture) # 가능한 최소값
r = sum(lecture) # 가능한 최대값

result = r # 최대값으로 초기화
while l <= r:
    mid = (l + r) // 2
    m_count = get_m_count(mid)

    if m_count <= M: # 조건을 만족하는 경우
        result = min(result, mid) # 최종 결과값 업데이트
        r = mid - 1
    else:
        l = mid + 1

print(result)