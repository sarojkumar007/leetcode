# solutions\1457. Pseudo-Palindromic Paths in a Binary Tree

Difficulty: `medium`

Topics: `Bit Manipulation`, `Tree`, `Depth-First Search`, `Breadth-First Search`, `Binary Tree`

## Q

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be **pseudo-palindromic** if at least one permutation of the node values in the path is a palindrome.

Return _the number of **pseudo-palindromic** paths going from the root node to leaf nodes_.

<br>

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2020/05/06/palindromic_paths_1.png)

```
Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2020/05/07/palindromic_paths_2.png)

```
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
```

Example 3:

```
Input: root = [9]
Output: 1
```

Constraints:

- The number of nodes in the tree is in the range `[1, 10`<sup>`5`</sup>`]`.
- `1 <= Node.val <= 9`

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
```
