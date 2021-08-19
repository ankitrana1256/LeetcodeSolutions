class Solution:
    def search(nums, target):
        try:
            index = nums.index(target)
        except:
            index = -1
        return index
        
    
nums = [4,5,6,7,0,1,2]
target = 3
a = Solution.search(nums, target)
print(a)