def plusOne(digits):
    temp = ''
    for i in digits:
        temp = temp + str(i)
        final = int(temp)+1
    return [s for s in str(final)]


print(plusOne([1,2,3]))
