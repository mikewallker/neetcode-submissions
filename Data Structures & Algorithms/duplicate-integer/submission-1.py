class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # //create set
        # //if elements in the set not equal the array length, output true
        # set_var = set(nums)
        # if len(set_var) == len(nums):
        #     return False
        # return True
        # brute force
        # we need to track list of number that are already found, call it trackList
        # and every time we acess a new item, we iterate the trackList to find the matching number
        trackList = []
        for item in nums:
            if item in trackList:
                return True
            trackList.append(item)
        return False