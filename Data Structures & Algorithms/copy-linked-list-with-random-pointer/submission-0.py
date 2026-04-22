"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}
        curr = head

        # The original value of the copied node
        while curr:
            nodeMap[curr] = Node(curr.val)
            curr = curr.next
        curr = head

        # next and random pointers to the new node corresponding to the next/random pointer of the original node
        while curr:
            newNode = nodeMap[curr]
            newNode.next = nodeMap.get(curr.next)
            newNode.random = nodeMap.get(curr.random)
            curr = curr.next
        return nodeMap.get(head)




        