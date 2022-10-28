def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(item for item in s if item.isalnum())

    # last index in array
    last = -1

    for letter in range(len(s)):
        if s[letter] == s[last]:
            last = last - 1
        else:
            return False
    return True

obj = isPalindrome("A man, a plan, a canal: Panama")
print(obj)