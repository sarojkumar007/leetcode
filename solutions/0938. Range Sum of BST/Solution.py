from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # 0 will be added if no root found
        if not root:
            return 0

        # go to left if high value found, as right won't be part of low:high
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        # go to right if low value found, as left won't be part of low:high
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # traverse both sides and add values, as it would fall under low:high
        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )
