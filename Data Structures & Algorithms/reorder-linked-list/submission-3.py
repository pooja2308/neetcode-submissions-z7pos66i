# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head.next or not head.next.next:
            return 
        # split the list to mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p2 = slow.next
        slow.next = None

        # reverese the list
        prev = None
        while p2:
            temp = p2.next
            p2.next = prev
            prev = p2
            p2 = temp
        p2 = prev 
        # Merge the list
        p1 = head
        while p2:
            p1next = p1.next
            p2next = p2.next
            p1.next = p2
            p2.next = p1next
            p1 = p1next
            p2 = p2next


        