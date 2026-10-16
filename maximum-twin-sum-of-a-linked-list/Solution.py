# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        rev=None
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        while slow:
            t=slow.next
            slow.next=rev
            rev=slow
            slow=t
        m=0
        while rev:
            m=max(head.val+rev.val,m)
            head=head.next
            rev=rev.next
        return m