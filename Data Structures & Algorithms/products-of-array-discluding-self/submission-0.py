class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMulti = [0] * len(nums)
        rightMulti = [0] * len(nums)
        # left[0] = 1
        # left[1] = item[0] * left[0]
        # left[2] = item[1] * left[1]
        # left[3] = item[2] * left[2]
        # ....
        leftMulti[0] = 1
        for i in range(1, len(nums)):
            leftMulti[i] = nums[i-1]*leftMulti[i-1]
        print(leftMulti)
        
        rightMulti[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            rightMulti[i] = nums[i+1]*rightMulti[i+1]
        print(rightMulti)

        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = leftMulti[i] * rightMulti[i]
        
        return result