# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        values = []
        
        def inorde(node):
            if node is None:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        for i in range(len(values)-1):
            if values[i] >= values[i+1]:
                return False
            
        return True
        