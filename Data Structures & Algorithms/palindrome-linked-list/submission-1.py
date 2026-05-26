# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        stackk = []
        while curr:
            stackk.append(curr.val)
            curr = curr.next

        # now iterate through linked list again and pop stackk element
        # check if the top ele is equal to head 
        while head:
            c = stackk.pop()
            if head.val != c:
                return False
            head = head.next

        return True
            
        