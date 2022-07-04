# def containsDuplicate(nums):
#     if len(nums) == len(set(nums)):
#         return True
#     else:
#         return False

def containsDuplicate(nums):
    map = []
    for i in range(0,len(nums)):
        if nums[i] not in map:
            map.append(nums[i])
    print(map)
    return map==nums




print(containsDuplicate([1,2,3,4]))