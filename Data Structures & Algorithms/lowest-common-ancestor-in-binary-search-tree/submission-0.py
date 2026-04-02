# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def check_ancestor(root):
            if not root:
                return None

            if root.val == p.val or root.val == q.val:
                return root

            left_tree = check_ancestor(root.left)
            right_tree = check_ancestor(root.right)

            if left_tree and right_tree:
                return root

            return left_tree or right_tree
        return check_ancestor(root) 
             

        