# solutions\0931. Minimum Falling Path Sum

Difficulty: `medium`

Topics: `Array`, `Dynamic Programming`, `Matrix`

## Q

Given an `n x n` array of integers `matrix`, return _the **minimum sum** of any **falling path** through `matrix`_.

A **falling path** starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

<br>

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg)

```
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg)

```
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
```

Constraints:

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 100`
- `-100 <= matrix[i][j] <= 100`

## S

### Python

#### Solution 1

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        cache = {}

        def dfs(r,c):
            if r == n:
                return 0

            if c < 0 or c == n:
                return float('inf')

            if (r,c) in cache:
                return cache[(r,c)]

            res = matrix[r][c] + min(
                dfs(r+1,c-1),
                dfs(r+1,c),
                dfs(r+1,c+1)
            )

            cache[(r,c)] = res
            return res

        res = float('inf')
        for c in range(n):
            res = min(res,dfs(0,c))

        return res
```

#### Solution 2

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for r in range(1,n):
            for c in range(n):
                mid = matrix[r-1][c]
                left = matrix[r-1][c-1] if c > 0 else float('inf')
                right = matrix[r-1][c+1] if c < n - 1 else float('inf')

                matrix[r][c] = matrix[r][c] + min(left, mid, right)

        return min(matrix[-1])
```
