# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateBST(root, float('-inf'), float('inf'))
    def validateBST(self, root, minVal, maxVal):

        if root is None:
            return True
        
        if root.val <= minVal or root.val >= maxVal:
            return False
        
        return self.validateBST(root.left, minVal, root.val) and self.validateBST(root.right, root.val, maxVal)
