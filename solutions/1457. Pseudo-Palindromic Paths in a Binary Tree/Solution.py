from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        cnt = defaultdict(int)
        odd = 0

        def dfs(r):
            nonlocal odd
            if not r:
                return 0
            
            cnt[r.val] += 1
            odd_change = 1 if cnt[r.val] % 2 else -1
            odd += odd_change

            if not r.left and not r.right:
                res = 1 if odd <= 1 else 0 # at leaf, if odd is 1 or 0, means its palindrome
            else:
                res = dfs(r.left) + dfs(r.right)
            
            odd -= odd_change
            cnt[r.val] -= 1
            return res
        
        return dfs(root)