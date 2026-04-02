# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # def identical(root, subRoot):
        #     if not root and not subRoot:
        #         return True
        #     if not root or not subRoot:
        #         return False
            
        #     return ((root.val == subRoot.val) and identical(root.left, subRoot.left) and identical(root.right, subRoot.right))
        
        # if not root:
        #     return False
        # if not subRoot:
        #     return True
        # if identical(root, subRoot):
        #     return True
        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        def serialized(node):
            if not node:
                return "£"
            return ("," + str(node.val) + serialized(node.left) + serialized(node.right))
        root_str = serialized(root)
        subroot_str = serialized(subRoot)
        return subroot_str in root_str
        


        