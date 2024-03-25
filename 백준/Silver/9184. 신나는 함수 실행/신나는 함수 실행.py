w = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
for i in range(1,len(w)):
    for j in range(1,len(w[0])):
        for k in range(1,len(w[0][0])):
            if i < j and j < k:
                w[i][j][k] = w[i][j][k-1] + w[i][j-1][k-1] - w[i][j-1][k]
            else:
                w[i][j][k] = w[i-1][j][k] + w[i-1][j-1][k] + w[i-1][j][k-1] - w[i-1][j-1][k-1]

while True:
    a,b,c = map(int,input().split())
    if a == b == c == -1:
        break
    elif a <= 0 or b <= 0 or c <= 0:
        print("w(%d, %d, %d) = 1" % (a,b,c))
        continue
    elif a > 20 or b > 20 or c > 20:
        print("w(%d, %d, %d) = %d" % (a,b,c,w[20][20][20]))
        continue
    else:
        print("w(%d, %d, %d) = %d" % (a,b,c,w[a][b][c]))