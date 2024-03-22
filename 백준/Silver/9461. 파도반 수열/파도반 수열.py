T = int(input())

for _ in range(T):
    N = int(input())
    d_base = [0, 1, 1, 1, 2, 2]
    d = [0] * (N+1)
    for i in range(1,N+1):
        if i <= 5:
            d[i] = d_base[i]
        else:
            d[i] = d[i-5] + d[i-1]
    print(d[N])