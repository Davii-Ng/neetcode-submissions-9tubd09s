# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxheight = 0
        def dfs(root):
            if not root:
                return 0
            left =  1 + dfs(root.left) 
            right = 1 + dfs(root.right)
            diameter = left + right - 1
            self.maxheight = max(self.maxheight, diameter)
            return max(left, right)
        dfs(root)
        return self.maxheight - 1