# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
6:04
"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # out = []


#         def helper1(node, out):    
#             if node:
#                 helper1(node.left, out)
#                 out.append(node.val)
#                 helper1(node.right, out)
                        
#         helper1(root, out)
#         return out
    
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res