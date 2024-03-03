# solutions\0513. Find Bottom Left Tree Value

Difficulty: `medium`

Topics: `Tree`, `Depth-First Search`, `Breadth-First Search`, `Binary Tree`

## Q

Given the `root` of a binary tree, return _the leftmost value in the last row of the tree_.

<br>

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg)

```
Input: root = [2,1,3]
Output: 1
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg)

```
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
```

Constraints:

- The number of nodes in the tree is in the range `[1, 10`<sup>`4`</sup>`]`.
- `-2`<sup>`31`</sup>` <= Node.val <= 2`<sup>`31`</sup>` - 1`

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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        while q:
            ans = q[0].val
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
```
