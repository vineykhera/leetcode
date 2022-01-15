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
    
        out = []
        st = []
        st.append((root, False))
        while st:
            node, visited = st.pop()
            if node:
                if visited:
                    out.append(node.val)
                else:
                    st.append((node.right, False))
                    st.append((node, True))
                    st.append((node.left, False))
        # print(out)
        return out
