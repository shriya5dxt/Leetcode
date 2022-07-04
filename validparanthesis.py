def isValid(s: str):
    stack = []
    dict =  {'{': '}', '[': ']', '(': ')'}
    for i in s:
        if i in dict.keys():
            stack.append(i)
            print(stack)
        if i in dict.values():
            if not stack:
                print(stack)
                return False
            elif i != dict[stack.pop()]:
                return False
    return stack == []


print(isValid('{}'))