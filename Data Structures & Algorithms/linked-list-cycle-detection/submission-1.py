# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        firstPtr = head
        secondPtr = head
        while(secondPtr):
            firstPtr = firstPtr.next
            if secondPtr.next is not None:
                secondPtr = secondPtr.next.next
            else:
                return False
            if(firstPtr == secondPtr):
                return True
        return False

        