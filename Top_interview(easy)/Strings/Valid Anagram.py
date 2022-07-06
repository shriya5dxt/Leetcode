def isAnagram(s, t) :
    if len(s) != len(t):
        return False
    t = list(t)
    for i in range(len(s)):
            if s[i] in t :
                t.remove(s[i])
    return len(t)==0

print(isAnagram("ana","naa"))