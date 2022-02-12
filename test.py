

def rotate_90(table):
    lth = len(table[0])
    tmp_table = [[0] * lth for _ in range(lth)] # 0으로 초기화

    for i in range(lth):
        for j in range(lth):
            tmp_table[i][j] = table[lth-1-j][i]

    return tmp_table


arr = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7],
    [4,5,6,7,8],
    [5,6,7,8,9]
]
for row in rotate_90(arr):
    print(row)

print([[] * 5 for _ in range(5)])

class BlockNumber:
    def __init__(self, num):
        self.value = num
        self.flag = 0

test = [[BlockNumber(0)] * 5 for _ in range(5)]

test[2][1].value = 3
test[2][4].value = 2

print(test[2][1].value)

for row in test:
    for v in row:
        print(v.value, end=' ')
    print()

print([[BlockNumber(0)] * 5 for _ in range(5)])

