N = int(input())

plus = []
minus = []
for _ in range(N):
    num = int(input())
    if num > 0:
        plus.append(num)
    else:
        minus.append(num) # 0 포함

plus.sort() # 0 보다 큰 숫자 오름차순 정렬
minus.sort(reverse=True) # 0 이하 숫자 내림차순 정렬

# print(plus) # test
# print(minus) # test

total_sum = 0
while len(plus) > 1: # 큰 숫자부터 짝수개 묶기
    a = plus.pop()
    b = plus.pop()
    if a == 1 or b == 1: # 숫자 중 1이 있을 경우
        total_sum += a + b
    else:
        total_sum += a * b

if len(plus) > 0: # 남은 숫자 1개 더하기
    total_sum += plus[0]

while len(minus) > 1: # 절대값 큰 숫자부터 짝수개 묶기
    a = minus.pop()
    b = minus.pop()
    total_sum += a * b

if len(minus) > 0: # 남은 숫자 1개 더하기
    total_sum += minus[0]

print(total_sum)