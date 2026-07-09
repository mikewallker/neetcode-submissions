class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,0]

        sortedNum = sorted(nums) # [-1,0,0,1]
        dictPair = {}
        resCandidate = set()
        result = []

        j = 2000
        zeroCount = 0
        for i in range(0, len(sortedNum)):
            if sortedNum[i] < 0:
                continue
            elif sortedNum[i] == 0:
                zeroCount += 1
            else:
                j = i # j is the first element positive
                break

        if (j == 2000) and zeroCount >= 3:
            return [[0,0,0]]
        elif (j == 2000) and zeroCount < 3:
            return []
            

        # for negative side + 0
        resCandidate.add(sortedNum[0])
        for i in range(0, j-1):
            num1 = sortedNum[i]
            for k in range (i+1, j):
                num2 = sortedNum[k]
                res = num1 + num2
                # num1 and num2 should be the same as num2,num1
                if (num1,num2) not in dictPair and (num2,num1) not in dictPair:
                    dictPair[(num1,num2)] = abs(res) # i want to find this
                resCandidate.add(num2) # i can give this
        
        # for positive side
        resCandidate.add(sortedNum[j])
        for i in range(j, len(sortedNum) - 1):
            for k in range (i+1, len(sortedNum)):
                num1 = sortedNum[i]
                num2 = sortedNum[k]
                res = num1 + num2
                if (num1,num2) not in dictPair and (num2,num1) not in dictPair: 
                    dictPair[(num1,num2)] = -(res) # i want to find this
                resCandidate.add(num2) # i can give this

        # so we have set and dictionary
        for key,value in dictPair.items():
            if value in resCandidate:
                result.append([key[0], key[1], value])

        if(zeroCount < 3 and [0,0,0] in result):
            result.remove([0,0,0])
        return result

        


    
        
        