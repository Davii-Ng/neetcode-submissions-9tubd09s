"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Approach: DFS + Hash Map

        Quick Explanation:
        1. Create a dictionary mapping original -> clone.
        2. If a node was cloned already, reuse its copy.
        3. Otherwise, create its clone and save it.
        4. Recursively clone each neighbor.
        5. Return the cloned starting node.

        Time Complexity: O(V + E)
        - Visit every node and connection.

        Space Complexity: O(V)
        - Hash map and recursion stack.
        """
        clones = {}

        def dfs(curr):
            if curr in clones:
                return clones[curr]

            clone = Node(curr.val)
            clones[curr] = clone

            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            
            return clone
        
        if not node:
            return None

        return dfs(node)

            