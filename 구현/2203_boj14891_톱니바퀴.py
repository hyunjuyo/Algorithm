def do_rotation(w, d):
    tmp = [0] * 8
    for i in range(8):
        ni = (i + d + 8) % 8
        tmp[ni] = wheel[w][i]
    wheel[w] = tmp[:] # 회전된 결과 반영
    rotate_check[w] = True # 회전여부 반영

def do_action(w, d):
    flag_l, flag_r = 0, 0
    if rotate_check[w]:
        return
    else:
        if w != 1 and wheel[w][6] != wheel[w-1][2]: # 좌측 인접 톱니바퀴 회전필요할 경우
            flag_l = 1
        if w != 4 and wheel[w][2] != wheel[w+1][6]: # 우측 인접 톱니바퀴 회전필요할 경우
            flag_r = 1
        do_rotation(w, d)
    if flag_l:
        do_action(w-1, -d)
    if flag_r:
        do_action(w+1, -d)

def get_score(wheel):
    score = 0
    for i in range(1, 5):
        if wheel[i][0] == 0:
            score += 0
        else:
            score += 2**(i-1)
    return score

wheel = [0]
for _ in range(4):
    wheel.append(list(map(int, list(input()))))
K = int(input())
for _ in range(K):
    w, d = map(int, input().split())
    rotate_check = [False] * 5
    do_action(w, d)
    # for v in wheel: # test
    #     print(v)

score = get_score(wheel)
print(score)