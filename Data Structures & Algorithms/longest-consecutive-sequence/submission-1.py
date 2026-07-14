class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequenceCount = {}
        for items in nums:
            if items-1 not in nums:
                sequenceCount[items] = 1
                currentSequence = items
                while currentSequence+1 in nums:
                    sequenceCount[items] += 1
                    currentSequence += 1

        firstIteration = True
        for sequence in sequenceCount:
            if firstIteration == True:
                maxValue = sequenceCount[sequence]
                firstIteration = False
            if sequenceCount[sequence] > maxValue:
                maxValue = sequenceCount[sequence]
        if len(nums) == 0:
            return 0
        return maxValue



