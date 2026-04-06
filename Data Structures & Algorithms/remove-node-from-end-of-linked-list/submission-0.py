# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        dummy2 = head
        length = 0
        tracker = 0

        while dummy:
            length += 1
            dummy = dummy.next
        
        if n == length:
            return head.next

        current = head
        for _ in range(length-n-1):
            current = current.next
        
        current.next = current.next.next

        return head

        