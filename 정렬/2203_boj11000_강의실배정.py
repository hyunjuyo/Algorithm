import sys
from collections import deque

N = int(input())
arr = []
for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    arr.append((S, T))

arr.sort(key=lambda x:(x[1], x[0]))

info = {}
room = 1

q = deque(arr)
s_time, t_time = q.popleft()
info[room] = [(s_time, t_time)] # 첫번째 강의 추가
while q:
    (s, t) = q.popleft()
    flag = False # 강의실 배정 여부
    for room_num, lecture_list in info.items(): # 기 배정된 강의실별로 마지막 강의 시간 확인
        t_time = lecture_list[-1][1] # 마지막 강의 종료 시간
        if t_time <= s:
            info[room_num].append((s, t))
            flag = True
            break
    if flag == False: # 기존 강의실에 배정이 안 된 경우
        room += 1
        info[room] = [(s, t)] # 강의실 새로 배정

    print(info) # test

print(len(info.keys()))