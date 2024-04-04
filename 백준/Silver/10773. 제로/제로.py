import sys

K = int(sys.stdin.readline())
nums = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if num != 0:
        nums.append(num)
    else:
        nums.pop()
print(sum(nums))