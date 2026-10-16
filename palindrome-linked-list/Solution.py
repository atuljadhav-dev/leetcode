# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # find mid of linked list
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # reverse and store the second half
        rev=None
        while slow :
            t=slow.next
            slow.next=rev
            rev=slow
            slow=t
        # iterate through original list and reversed list until reversed list end if val mismatch return False
        while rev:
            if head.val!=rev.val:
                return False
            head=head.next
            rev=rev.next
        return True