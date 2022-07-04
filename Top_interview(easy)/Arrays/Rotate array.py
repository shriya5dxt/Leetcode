# def rotate(nums,k):
#     y = []
#     for j in range(k,0,-1):
#         print(j)
#         for i in range(0,len(nums)):
#             x = nums.pop()
#             y.append(x)
#         print(y)
#         nums=y
#     return y

def rotate(nums,k):
    y=[]
    while k>0:
        nums.insert(0, nums[-1])
        nums.pop()
        k -= 1
    return(nums)


print(rotate([1,2,3,4],3))