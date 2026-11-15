# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        BFS approach
        """

        q_p = deque([p])
        q_q = deque([q])

        while q_p and q_q:
            node_p = q_p.popleft()
            node_q = q_q.popleft()

            if not node_p and not node_q:
                continue

            if not node_p or not node_q or node_p.val != node_q.val:
                return False

            q_p.append(node_p.left)
            q_q.append(node_q.left)
            q_p.append(node_p.right)
            q_q.append(node_q.right)

        return True