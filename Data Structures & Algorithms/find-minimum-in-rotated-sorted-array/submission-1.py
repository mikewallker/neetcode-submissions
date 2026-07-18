class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        # [3,4,5] and [6,1,2]
        # min=3 [6] and [1,2]
        # min=1
        # base case array length 1
        # [4,5,0,1,2,3]
        # [4,5,0] and [1,2,3] min = 1
        # [4] and  [5,0] min = 1
        # [5] and [0] min 0
        # smallestItem = nums[0] #only needed once
        # if len(nums) == 1:
        #     if nums[0] < smallestItem:
        #         return nums[0]
        # middleIdx = len(nums)/2
        # leftArray = nums[0:middleIdx]
        # rightArray = nums[middleIdx:]
        # if leftArray[0] > leftArray[middleIdx-1]:
        #     findMin(self, leftArray)
        # if leftArray[0] > leftArray[middleIdx-1]:
        #     findMin(self, leftArray)

        #when we stop? 1. whenn the array length is 1. 2. when the first item is smaller than the last item
        # [4,5,0,1,2,3]
        minItem = nums[0] # 1
        while True:
            if(len(nums) == 1):
                return nums[0]
            print("nums: " + str(nums))
            if nums[0] < nums[len(nums) - 1]:
                return min(nums[0], minItem)
            middleIdx = math.floor(len(nums)/2) # 1
            leftArray = nums[0:middleIdx] # [5]
            rightArray = nums[middleIdx:] # [0]
            print("leftArray: " + str(leftArray))
            print("rightArray: " + str(rightArray))
            # check if array is 1 or not
            if len(leftArray) == 1:
                minItem = min(minItem, leftArray[0])
                if len(rightArray) != 1:
                    nums = rightArray
                    continue
                else:
                    minItem = min(minItem, rightArray[0])
                    return minItem
            
            # check if array 2 item with in order
            # check 2 item not in order
            # we choose which subarray will become our current array
            if leftArray[0] < leftArray[len(leftArray) - 1]:
                minItem = min(minItem, leftArray[0])
                nums = rightArray
            else:
                minItem = min(minItem, rightArray[0]) # 1
                nums = leftArray
