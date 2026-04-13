# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        def rightSideRec(root, level, result):
            if not root:
                return None

            if len(result) == level:
                result.append(root.val)

            rightSideRec(root.right, level+1, result)
            rightSideRec(root.left, level+1, result)
            
        rightSideRec(root, 0, res)   
        return res


            




        