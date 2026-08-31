# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count ll length
        ptrCount = head
        count = 1
        while ptrCount.next != None:
            ptrCount = ptrCount.next
            count += 1
        
        # find the node position we want to remove
        # we actually want to find the exact position and prev position
        # when we find the prev, the target node just the enxt of it
        position = count - n
        if position == 0:
            return head.next
        positionPtr = head
        current = 1
        while current != position:
            positionPtr = positionPtr.next
            current += 1
        
        # remove the node
        temp = positionPtr.next
        positionPtr.next = temp.next
        temp.next = None


        # return
        return head
        