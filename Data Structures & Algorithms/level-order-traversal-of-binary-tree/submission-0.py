# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def levelOrderRecursion(root, level, res):
            if not root:
                return None
            
            if len(res) <= level:
                res.append([])

            res[level].append(root.val)

            levelOrderRecursion(root.left, level + 1, res)
            levelOrderRecursion(root.right, level + 1, res)
        levelOrderRecursion(root, 0, res)
        return res

        