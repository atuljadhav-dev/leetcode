# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None #end of the list
        curr=head
        while curr!=None:
            t=curr.next #store the next node
            curr.next=prev #reverse the link
            prev=curr # move prev to current 
            curr=t # move curr to the next node
        return prev
        # ex [1,2,3,None]
        # prev=[None], curr=1, t=2
        # t=curr.next i.e 2
        # curr.next=prev i.e 1.next=None
        # prev=curr i.e prev=1
        # curr=t i.e curr=2
        # prev=[1,None], curr=2, t=3
        # t=curr.next i.e 3
        # curr.next=prev i.e 2.next=1
        # prev=curr i.e prev=2
        # curr=t i.e curr=3
        # prev=[2,1,None], curr=3, t=None
        # t=curr.next i.e None
        # curr.next=prev i.e 3.next=2
        # prev=curr i.e prev=3
        # curr=t i.e curr=None
        # return prev i.e [3,2,1,None]