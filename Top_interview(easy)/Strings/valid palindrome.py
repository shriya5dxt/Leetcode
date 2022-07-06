def isPalindrome(s: str) -> bool:
     temp = list(''.join(s.split(' ')))
     print([temp.pop().lower() for i in range(0,len(temp)-1) if temp[i].isalpha()])
     if s == [temp.pop() for i in range(len(temp))]:
         return True
     else:
         return False

obj = isPalindrome("A man, a plan, a canal: Panama")
print(obj)