class Solution:
    
    nums = [3,6,2,3]

    def largestPerimeter(nums):
        
        nums.sort(reverse =True)
        print(nums)
        for i in range(len(nums)):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
            else:
                return 0
    print(largestPerimeter(nums))

