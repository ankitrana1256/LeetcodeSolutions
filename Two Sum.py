nums = [3,3]
target = 6

for i in range(len(nums)):
    temp = target - nums[i]
    if temp in nums:
        temp_index = nums.index(temp)
        if temp_index != i:
            pass
        else:
            arr = nums[:temp_index]
            arr.insert(temp_index,-1)
            arr.extend(nums[temp_index + 1:])
            if temp in arr:
                print(i,arr.index(temp))