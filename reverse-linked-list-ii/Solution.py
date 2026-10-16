# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:
        if right == left:
            # single node reverse
            return head
        if not head:
            # empty list
            return None
        pos = 1
        t = head
        before = None
        while t and left != pos:
            # find node from which nedd to reverse
            before = t
            t = t.next
            pos += 1
        curr = t
        prev = None
        n = right - left + 1
        while n != 0:
            # reverse
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            n -= 1
        # attach the remaining list
        t.next = curr
        if before:
            # attach the reversed list to start
            before.next = prev
            return head
        # if left is 1
        return prev

