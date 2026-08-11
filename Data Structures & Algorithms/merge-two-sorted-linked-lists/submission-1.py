# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resultHead = None
        resultPtr = None
        while list1 is not None or list2 is not None:
            if list1 is None:
                if resultHead is None:
                    resultHead = list2
                else:
                    resultPtr.next = list2
                break
            elif list2 is None:
                if resultHead is None:
                    resultHead = list1
                else:
                    resultPtr.next = list1
                break
            if list1.val > list2.val:
                if resultHead is not None:
                    resultPtr.next = list2
                    resultPtr = resultPtr.next
                else:
                    resultHead = list2
                    resultPtr = list2
                list2 = list2.next
            else:
                if resultHead is not None:
                    resultPtr.next = list1
                    resultPtr = resultPtr.next
                else:
                    resultHead = list1
                    resultPtr = list1
                list1 = list1.next
        return resultHead
            
            
        