class Solution:
    def findDuplicates(nums):
        visited = set()
        array = []
        
        for i in range(len(nums)):
            if nums[i] in visited:
                array.append(nums[i])
            else:
                visited.add(nums[i]) 
        return array
                
nums = [4,3,2,7,8,2,3,1]
a = Solution.findDuplicates(nums)
print(a)