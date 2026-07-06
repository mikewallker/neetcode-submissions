class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # //create set
        # //if elements in the set not equal the array length, output true
        set_var = set(nums)
        if len(set_var) == len(nums):
            return False
        return True