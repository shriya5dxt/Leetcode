# def two_sum(nums, target):
#     a = 0
#     d = []
#     for i in range(len(nums)):
#         temp = target - nums[i]
#         print(temp)
#         if temp in d:
#             return [d[temp],i]
#         d[nums[i]] = i

# print(twoum([3,8,11,15,1],12))

# def two_sum(nums,target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i<j and (nums[i] + nums[j] == target):
#                 return [i,j]

# def two_sum(nums,target):
#     for i in range(len(nums)):
#         temp = target - nums[i]
#         if temp in nums:
#             for j in range(len(nums)):
#                 if temp == nums[j]:
#                     return i,j

def two_sum(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
        # print(hashmap)
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in hashmap and hashmap[temp] !=i:
            return [i,hashmap[temp]]



print(two_sum([3,8,11,15,1],12))