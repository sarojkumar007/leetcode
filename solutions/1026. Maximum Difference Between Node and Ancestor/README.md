# solutions\1026. Maximum Difference Between Node and Ancestor

Difficulty: `medium`

Topics: `Tree`, `Depth-First Search`, `Binary Tree`

## Q

Given the `root` of a binary tree, find the maximum value `v` for which there exist **different** nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor of `b`.

A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b` or any child of `a` is an ancestor of `b`.

<br>

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg)

```
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg)

```
Input: root = [1,null,2,null,0,3]
Output: 3
```

Constraints:

- The number of nodes in the tree is in the range `[2, 5000]`.
- `0 <= Node.val <= 10`<sup>`5`</sup>

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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_min, curr_max):
            if not node:
                return curr_max - curr_min

            curr_min = min(curr_min, node.val)
            curr_max = max(curr_max, node.val)

            return max(dfs(node.left, curr_min, curr_max), dfs(node.right, curr_min, curr_max))

        return dfs(root, root.val, root.val)
```
