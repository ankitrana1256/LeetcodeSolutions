class Solution:
    def findMin(nums):
        temp = nums[0]
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                pass
            else:
                temp = nums[i+1]
                break
                
        return temp
            
nums = [4,5,6,7,8,9,1]
a = Solution.findMin(nums)
print(a)