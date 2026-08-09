class Solution:
    def minWindow(self, s: str, t: str) -> str:
        print("a")
        charCounter = {}
        leftIdx = 0
        rightIdx = 0
        resultString = ""
        candidateString = ""
        
        # tIsPresent = False 
        tUniqueCtr = 0
        substringUniqueCtr = 0
        dictCountT = {}
        for char in t:
            if char not in dictCountT:
                dictCountT[char] = 1
                tUniqueCtr += 1
            else:
                dictCountT[char] += 1

        #base case
        if len(t) == 1 and t in s:
            return t
        
        # assigning leftIdx
        while leftIdx != len(s):
            if s[leftIdx] in t:
                charCounter[s[leftIdx]] = 1
                if charCounter[s[leftIdx]] == dictCountT[s[leftIdx]]:
                    substringUniqueCtr += 1
                break
            leftIdx += 1
        rightIdx = leftIdx + 1

        

        # start moving rightIdx
        while rightIdx < len(s):
            if s[rightIdx] in t:
                #update charCounter
                if s[rightIdx] not in charCounter:
                    charCounter[s[rightIdx]] = 1                    
                else:
                    charCounter[s[rightIdx]] += 1

                if charCounter[s[rightIdx]] == dictCountT[s[rightIdx]]:
                    substringUniqueCtr += 1
                
                
                # if not tIsPresent:
                #     ctr = 0
                #     for char in t:

                #         if char in charCounter and charCounter[char] >= dictCountT[char]:
                #             ctr+=1
                #     if ctr == len(t):
                #         tIsPresent = True
                # if tIsPresent:
                print(substringUniqueCtr)
                if substringUniqueCtr >= tUniqueCtr:
                    
                    while True:
                        if s[leftIdx] in t:
                            if charCounter[s[leftIdx]] == dictCountT[s[leftIdx]]:
                                break
                            else:
                                charCounter[s[leftIdx]] -= 1
                        leftIdx += 1
                    candidateString = s[leftIdx:rightIdx+1]
                    print("a")
                    if len(candidateString) < len(resultString) or resultString == "":
                        resultString = candidateString[:]
            rightIdx += 1
        return resultString