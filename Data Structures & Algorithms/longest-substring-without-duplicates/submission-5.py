class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        leftIdx = 0
        rightIdx = 1
        maxSubsLen = 1
        tempSub = [s[0]] 
        currentSubLen = 1 
        tempSet = set([s[0]]) 
        # "aab"
        while rightIdx < len(s): # 3 < 3
            tempSet.add(s[rightIdx]) # [ab]
            if len(tempSet) == currentSubLen: #2 == 1
                # duplicate found
                # move left index
                for i in range(len(tempSub)): # for i in range(1)
                    if tempSub[i] == s[rightIdx]: # a == a
                        leftIdx += i + 1 # 0 + 0 + 1 = 1
                # reset the tracker
                
                tempSub = list(s[leftIdx:rightIdx+1]) # [a]
                currentSubLen = len(tempSub) # 1
                tempSet = set(tempSub) # [a]
            else:
                tempSub.append(s[rightIdx]) # [ab] 
                currentSubLen += 1 # 2
            rightIdx += 1 # 3
            # update max substring length                    
            if currentSubLen > maxSubsLen: # 2 > 1
                maxSubsLen = currentSubLen # 2
        return maxSubsLen
