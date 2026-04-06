# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0)
        tail = dummyhead
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1Num = l1.val if l1 else 0
            l2Num = l2.val if l2 else 0
            Sum = l1Num + l2Num + carry
            carry = Sum // 10
            newNode = ListNode(Sum % 10)
            tail.next = newNode
            tail = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyhead.next