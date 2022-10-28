def removeElement(nums, val):
    temp = []
    for i in range(len(nums)):
        if nums[i] == val:
            p_val = nums.pop(val)
            temp.append(p_val)
            print(temp)

print(removeElement([3,2,2,3],3))