def removeDuplicates(a):
    i = 0
    l = len(a) - 1
    while i < l:
        if a[i] == a[i + 1]:
            a[i + 1] ='_'
            l -= 1
        else:
            i += 1
    print(a)
    return a

removeDuplicates([1,1,2,2,2,2])

def removeDuplicates2(nums):
    i =0
    for j in (1,len(nums)-1):
        if nums[i] != nums[j]:
            i = i + 1
            nums[i] = nums[j]
        nums[j] ='_'
    print(nums)

removeDuplicates2([1,1,2,2,2,2])

