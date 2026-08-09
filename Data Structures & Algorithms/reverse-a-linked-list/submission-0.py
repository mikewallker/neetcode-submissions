# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev = head
        current = head.next
        temp = head.next.next
        while current != None:
            current.next = prev
            if prev == head:
                prev.next = None # only for head
            prev = current
            current = temp
            if temp != None:
                temp = temp.next
        return prev



        
        