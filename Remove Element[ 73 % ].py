class Solution:
    def removeElement(nums, val) -> int:
        i = 0
        while(i < len(nums)):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1
        l = len(nums)
        return l
        
        
nums = [0,1,2,2,3,0,4,2]
val = 2
a = Solution.removeElement(nums,val)
print("k :",a)
print(nums)