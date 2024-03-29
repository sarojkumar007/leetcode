from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(r):
            if not r:
                return -1
            
            left = dfs(r.left)
            right = dfs(r.right)

            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return res[0]