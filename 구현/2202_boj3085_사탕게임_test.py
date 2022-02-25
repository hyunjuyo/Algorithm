
def get_max_num(table):
    max_num = 0
    row_idx = -1
    col_idx = -1
    for i in range(N):
        color_list = [0, 0, 0, 0] # C,P,Z,Y
        for j in range(N):
            if table[i][j] == 'C':
                color_list[0] += 1
            elif table[i][j] == 'P':
                color_list[1] += 1
            elif table[i][j] == 'Z':
                color_list[2] += 1
            else:
                color_list[3] += 1
        if max(color_list) > max_num:
            max_num = max(color_list)
            row_idx = i
            col_idx = j
    
    return max_num, row_idx, col_idx


N = int(input())
table = []
for _ in range(N):
    table.append(list(input()))

for v in table:
    print(v)

max_num, row, col  = get_max_num(table)

print(max_num, row, col)