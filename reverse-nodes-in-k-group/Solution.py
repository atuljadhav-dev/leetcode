# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            # empty list
            return None
        if k == 1:
            return head
        curr = head
        before = None  # update the res list add new reverese nodes to it
        res = None  # store the head of res
        while curr:
            t = curr
            rev = None
            n = k
            rem = 0
            tmp = curr
            while tmp:
                # check remaining nodes count
                rem += 1
                tmp = tmp.next
            if rem < k:
                # if count is remaining is less than k return them as it is
                rev = curr
                t = None
            while n != 0 and t and rem >= k:
                # reverse the next k nodes
                nxt = t.next
                t.next = rev
                rev = t
                t = nxt
                n -= 1
            curr = t
            if not before:
                # store th res and reference
                before = rev
                res = before
            elif before:
                while before and before.next:
                    before = before.next
                    # update the res
                before.next = rev
        return res
