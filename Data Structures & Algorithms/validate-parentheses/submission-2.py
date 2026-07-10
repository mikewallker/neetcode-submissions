class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if(s[i] == "("
                or s[i] == "{"
                or s[i] == "["
                ):
                stack.append(s[i])
            else:
                # unopened
                if (len(stack) == 0):
                    return False
                poppedItem = stack.pop()
                if(s[i] == ")" and poppedItem == "("):
                    continue
                elif(s[i] == "}" and poppedItem == "{"):
                    continue
                elif(s[i] == "]" and poppedItem == "["):
                    continue
                else:
                    return False
        # unclosed
        if (len(stack) == 0):
            return True
        else:
            return False
                    
            