# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None:
            if subRoot is None:
                return True
            return False
        
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSameTree(self, nodeA, nodeB):

        if nodeA is None and nodeB is None:
            return True
        
        if nodeA and nodeB and nodeA.val == nodeB.val:
            return self.isSameTree(nodeA.left, nodeB.left) and self.isSameTree(nodeA.right, nodeB.right)
        
        return False