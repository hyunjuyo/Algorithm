import sys
from collections import deque

def check_room(arr, room):
    next_arr = []
    q = deque(arr)

    s_time, t_time = q.popleft()
    info[room] = [(s_time, t_time)] # 첫번째 강의 추가
    while q:
        (s, t) = q.popleft()
        if s < t_time:
            next_arr.append((s, t)) # 다음 강의실로 배정 검토
            continue
        else:
            info[room].append((s, t)) # 두번째 이후 강의 추가
            t_time = t # 기준 시간 업데이트
    
    return next_arr

N = int(input())
arr = []
for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    arr.append((S, T))

arr.sort(key=lambda x:(x[1], x[0]))

info = {}
room = 1
while arr:
    arr = check_room(arr, room)
    room += 1 # 강의실 번호 +1

    print(info) # test

print(len(info.keys()))