nums = [1,2,4,6]
target = 3
answer = 0
if target in nums:
    res = nums.index(target)
else:
    res = min(enumerate(nums), key=lambda x: abs(target - x[1]))
    res += 1
    print(res)