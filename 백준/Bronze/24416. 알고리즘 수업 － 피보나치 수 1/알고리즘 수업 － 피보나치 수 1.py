n = int(input())

count_fib, count_fibonacci = 0, 0

def fib(n):
    global count_fib
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

d = [0] * (n+1)
def fibonacci(n):
    global d, count_fibonacci
    d[1], d[2] = 1, 1
    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2]
        count_fibonacci += 1
    return d[n]

print(fibonacci(n), count_fibonacci)