# solutions\0543. Diameter of Binary Tree

Difficulty: `easy`

Topics: `Tree`, `Depth-First Search`, `Binary Tree`

## Q

Given the `root` of a binary tree, return _the length of the **diameter** of the tree_.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

<br>

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

Example 2:

```
Input: root = [1,2]
Output: 1
```

Constraints:

- The number of nodes in the tree is in the range `[1, 10`<sup>`4`</sup>`]`.
- `-100 <= Node.val <= 100`

## S

### Python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
```
