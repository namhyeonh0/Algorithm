def solution(nums):
    result = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                n = nums[i]+nums[j]+nums[k]
                count = 0
                for z in range(2,n):
                    if n % z == 0:
                        count += 1
                if count == 0:
                    result += 1
    
        
    return result