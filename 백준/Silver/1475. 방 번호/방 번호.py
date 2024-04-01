N = str(input())
nums = [0 for _ in range(10)]
for num in N:
    nums[int(num)] += 1

num6 = nums[6]
num9 = nums[9]
nums[6] = 0
nums[9] = 0
answer = max((num6+num9+1)//2,max(nums))
print(answer)