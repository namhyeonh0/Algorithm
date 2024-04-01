n = int(input())
nums = list(map(int,input().split()))
x = int(input())

nums.sort()

count = 0
left = 0
right = n-1

while left < right:
    now = nums[left] + nums[right]
    if now == x:
        count += 1
        left += 1
    elif now < x:
        left += 1
    else:
        right -= 1

print(count)