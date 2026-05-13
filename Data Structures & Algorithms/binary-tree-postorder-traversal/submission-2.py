# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postorder(root):
            if not root:
                return


            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res


        # res = []
        # stack = []
        # cur = root
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = cur.right 
        #     cur = stack.pop()
        #     res.append(cur.val)
            
        # return res
        
            
            
        