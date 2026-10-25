# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        l=1
        tail=head
        while tail and tail.next:
            # find length and store end of list
            tail=tail.next
            l+=1
        if l<2:
            return head
        k=k%l # actual  no of times need to rotate
        if k==0 or l==k:
            return head
            
        curr=head
        while l-k!=1 and curr and curr.next:
            # find the previous node of new linked list start node
            curr=curr.next
            l-=1
        res=curr.next #store start node
        temp=res
        curr.next=None #last node next to None
        tail.next=head #attach head to to end
        return res