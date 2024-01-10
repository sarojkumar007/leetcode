# solutions\2385. Amount of Time for Binary Tree to Be Infected

Difficulty: `medium`

Topics: `Tree`, `Depth-First Search`, `Breadth-First Search`, `Binary Tree`

## Q

You are given the `root` of a binary tree with **unique** values, and an integer `start`. At minute `0`, an **infection** starts from the node with value `start`.

Each minute, a node becomes infected if:

- The node is currently uninfected.
- The node is adjacent to an infected node.

Return _the number of minutes needed for the entire tree to be infected_.

<br>

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2022/06/25/image-20220625231744-1.png)

```
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2022/06/25/image-20220625231812-2.png)

```
Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
```

Constraints:

- The number of nodes in the tree is in the range `[1, 105]`.
- `1 <= Node.val <= 10`<sup>`5`</sup>
- Each node has a **unique** value.
- A node with a value of `start` exists in the tree.

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
```
