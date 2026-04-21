# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first let's take a dummy List which should be an object of ListNode
        dummy = ListNode()
        dummy.next = head

        # let's take two pointers and initialise it with head
        ahead = behind = dummy

        # now we need to loop ahead pointer n+1 times
        for _ in range(n+1):
            ahead = ahead.next  
        
        # we need to loop through until ahead pointer is beyond the loop and 
        # keep increaing both ahead and behind pointers
        while ahead:
            ahead = ahead.next
            behind = behind.next
        
        # so now behind.next is at the position where next elements should be deleted.
        # Assign behind.value to behind.next.next which is skipping n value 
        behind.next = behind.next.next
        return dummy.next