# solutions\0938. Range Sum of BST

Difficulty: `easy`

Topics: `Tree`, `Depth-First Search`, `Binary Search Tree`, `Binary Tree`

## Q

Given the `root` node of a binary search tree and two integers `low` and `high`, return _the sum of values of all nodes with a value in the **inclusive** range_ `[low, high]`.

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg)

```
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg)

```
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
```

Constraints:

- The number of nodes in the tree is in the range `[1, 2 * 10`<sup>`4`</sup>`]`.
- `1 <= Node.val <= 10`<sup>`5`</sup>
- `1 <= low <= high <= 10`<sup>`5`</sup>
- All `Node.val` are **unique**.

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

```
