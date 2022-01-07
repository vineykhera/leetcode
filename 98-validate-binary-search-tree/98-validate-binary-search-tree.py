# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(node, minval, maxval):
            if not node:
                return True
            if node.val > minval and node.val < maxval:
                return isvalid(node.left, minval, node.val) and isvalid(node.right, node.val, maxval)   
            else:
                return False
            
        return isvalid(root, float('-inf'), float('inf'))        
