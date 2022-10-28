def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    temp = []
    a =0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[a],nums[i] = nums[i],nums[a]
            a = a+1
            # nums[(len(nums)-1)] = nums[i]
    return nums


print(moveZeroes([0,1,0,3,12]))

