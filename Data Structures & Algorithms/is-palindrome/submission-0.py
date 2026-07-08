import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #consider only alphanumeric
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        # remove space
        s = re.sub(' ', '', s)
        #to lowercase
        s = s.lower()
        #empty
        # 1 char
        # 2 or more char
        if s == "" or len(s) == 1:
            return True
        # get 2 index from front and back
        # increment front, decrement back

        i = 0
        j = len(s) - 1
        while(i < j):
            if s[i] == s[j]:
                i+=1
                j-=1
                continue
            return False

        return True