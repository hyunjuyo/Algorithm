import math

x, y, c = map(float, input().split())

result = min(x, y)
l = 0.001
r = min(x, y) - 0.001
while l <= r:
    mid = (l + r) / 2

    # 높이가 c인 지점 찾기
    f_x = mid - (c / (math.sqrt(x**2 - mid**2) / mid))
    f_y = c / (math.sqrt(y**2 - mid**2) / mid)
    print('(f_x, f_y) :', f_x, f_y) # test

    if f_x <= f_y: # 너비가 넓은 경우
        r = mid - 0.001
        result = min(result, mid)
    else:
        l = mid + 0.001

print(result) # test
print(round(result, 3))