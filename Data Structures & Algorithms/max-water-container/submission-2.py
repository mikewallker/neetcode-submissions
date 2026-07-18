class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # long * height
        # subarray length-1 * min of 2 wall number
        currMax = 0
        # for i in range(len(heights)-1):
        #     for j in range(len(heights)-1, i, -1):
        #         currWater = len(heights[i:j])*min(heights[i], heights[j])
        #         if currWater > currMax:
        #             currMax = currWater
        # return currMax

        i = 0
        j = len(heights) - 1
        while i < j:
            currWater = len(heights[i:j])*min(heights[i], heights[j])
            if currWater > currMax:
                currMax = currWater
            if(heights[i] < heights[j]):
                i+=1
            else:
                j-=1
        return currMax

