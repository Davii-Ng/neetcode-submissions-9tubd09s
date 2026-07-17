# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def BFS(node):
            from collections import deque
            queue = deque()

            queue.append(node)

            while queue:
                x = queue.popleft()
                if x:
                    x.left, x.right = x.right, x.left
                    queue.append(x.left) 
                    queue.append(x.right) 
                

        BFS(root)
        return root

