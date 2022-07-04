def intersect(nums1, nums2):
    temp = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                temp.append(nums1[i])
                print(nums2)
                del nums2[j]
                print(nums2)
                break


    return temp
print(intersect([2], [2,2,9,8,4]))
