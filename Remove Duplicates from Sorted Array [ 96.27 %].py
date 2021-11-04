class Solution:
    def removeDuplicates(nums) -> int:
        new_list = list(set(nums))
        nums.clear()
        nums.extend(new_list)
        nums.sort()
        return len(nums)

nums = [1,1,2]
k = Solution.removeDuplicates(nums)
print(k, nums)