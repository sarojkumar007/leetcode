# solutions\0872. Leaf-Similar Trees

Difficulty: `easy`

Topics: `Tree`, `Depth-First Search`, `Binary Tree`

## Q

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a **leaf value sequence**.

![Ex](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png)

For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.

Two binary trees are considered _leaf-similar_ if their leaf value sequence is the same.

Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.

<br>

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg)

```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg)

```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
```

Constraints:

- The number of nodes in each tree will be in the range `[1, 200]`.
- Both of the given trees will have values in the range `[0, 200]`.

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
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        def dfs(root, leaf):
            if not root:
                return

            if not root.left and not root.right:
                leaf.append(root.val)
                return

            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        return leaf1 == leaf2
```

### TypeScript

```typescript
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function leafSimilar(root1: TreeNode | null, root2: TreeNode | null): boolean {
  function dfs(root: TreeNode | null, leaf: number[]) {
    if (!root) return;
    if (!root.left && !root.right) {
      leaf.push(root.val);
      return;
    }
    dfs(root.left, leaf);
    dfs(root.right, leaf);
  }

  const leaf1: number[] = [],
    leaf2: number[] = [];
  dfs(root1, leaf1);
  dfs(root2, leaf2);

  return (
    leaf1.length === leaf2.length &&
    leaf1.every((val, idx) => val === leaf2[idx])
  );
}
```
