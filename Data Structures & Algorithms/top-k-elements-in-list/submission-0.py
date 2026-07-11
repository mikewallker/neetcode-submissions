class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary count value
        # array [count, value]
        countDict = {}
        for item in nums:
            if item not in countDict:
                countDict[item] = 1
            else:
                countDict[item] += 1

        sortedDict = dict(sorted(countDict.items(), key=lambda item: item[1], reverse=True))
        counter = k
        result = []
        for key, value in sortedDict.items():
            if (counter > 0):
                counter -=1
            elif(counter == 0):
                break
            result.append(key)
        return result
        