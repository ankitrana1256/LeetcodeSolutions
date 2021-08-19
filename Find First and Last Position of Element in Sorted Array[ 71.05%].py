class Solution:
    def searchRange(nums, target):
        new = []
        try:
            a =  nums.index(target)
            b = nums[::-1].index(target)
            c = len(nums) - b - 1
        except:
            a, c = -1,-1
        new.append(a)
        new.append(c)
        return new
    
nums = [5,7,7,6,8,8,10]
target = 6
a = Solution.searchRange(nums,target)
print(a)