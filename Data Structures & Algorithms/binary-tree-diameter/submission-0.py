# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            left_path = dfs(curr.left)
            right_path = dfs(curr.right)
            self.res = max(self.res, left_path + right_path)
            return 1 + max(left_path, right_path)
        dfs(root)
        return self.res

            