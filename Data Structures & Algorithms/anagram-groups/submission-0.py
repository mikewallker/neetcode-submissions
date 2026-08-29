class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a sorted version of each word
        sortedStrs = []
        for word in strs:
            sortedWord = "".join(sorted(word))
            sortedStrs.append(sortedWord)
        # create a result dictionary 
        res = {}
        # key: sortedWord value: array of original word
        for i in range(len(sortedStrs)):
            # exist in ict
            if sortedStrs[i] in res:
                res[sortedStrs[i]].append(strs[i])
            # not exist yet
            else:
                res[sortedStrs[i]] = []
                res[sortedStrs[i]].append(strs[i])
        realRes = []
        for item in res:
            realRes.append(res[item])
        return realRes

