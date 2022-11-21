mat = []

for i in range(256):
    row = list(map(int,input().split()))
    mat.append(row)

tp = 256
left = 256

rt = 0
btm = 0

len_row = len(mat)
len_col = len(mat[0])

for i in range(0,len_row):
    start = 0
    while(start < len_col):
        if (mat[i][start] == 0):
            left = min(left,start)
            break
        start+=1
    
    end = len_col - 1
    while(end >=0 ):
        if(mat[i][end] == 0):
            rt = max(end,rt)
            break
        end -= 1

    tp_start = 0
    while(tp_start < len_row):
        if (mat[tp_start][i] == 0):
            tp = min(tp,tp_start)
            break
        tp_start+=1

    btm_end = len_row - 1
    while(btm_end >= 0):
        if (mat[btm_end][i] == 0):
            btm = max(btm,btm_end)
            break
        btm_end-=1

print((tp,left),(tp,rt),(btm,left),(btm,rt))