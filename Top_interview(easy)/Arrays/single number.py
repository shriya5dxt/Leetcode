def singleNumber(nums):
    for i in range(len(nums)):
        if (nums[i] not in nums[i + 1:]) and (nums[i] not in nums[:i]):
            return nums[i]





print(singleNumber([2,2,3,3,4]))