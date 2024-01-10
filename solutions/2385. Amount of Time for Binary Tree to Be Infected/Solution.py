from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def connectParent(node, parent):
            if node is None:
                return
            node.parent = parent

            connectParent(node.left, node)
            connectParent(node.right, node)

        connectParent(root, None)

        found = None

        def findNode(node):
            if node is None:
                return

            if node.val == start:
                nonlocal found
                found = node

            findNode(node.left)
            findNode(node.right)

        findNode(root)
        assert found is not None  # revise

        def findFarthest(node, prev, depth):
            farthest = 0
            for nextNode in [node.left, node.right, node.parent]:
                if nextNode is not None and nextNode != prev:
                    farthest = max(
                        farthest, findFarthest(nextNode, node, depth + 1) + 1
                    )  # revise for +1
            return farthest

        return findFarthest(found, None, 0)
