def longestCommonPrefix(strs) -> str:
    list.sort(strs)
    result = ""

    if len(strs) == 1:
        return strs[0]

    for j in range(len(strs[0])):
        for i in range(len(strs) - 1):
            m1, m2 = strs[i], strs[i + 1]
            if m1[j] != m2[j]:
                return result
        result += m1[j]

    return result

print(longestCommonPrefix(["flower","flow","flight"]))