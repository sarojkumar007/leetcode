# solutions\2482. Difference Between Ones and Zeros in Row and Column

Difficulty: `medium`

Topics: `Array`, `Matrix`, `Simulation`

## Q

You are given a **0-indexed** `m x n` binary matrix `grid`.

A **0-indexed** `m x n` difference matrix `diff` is created with the following procedure:

- Let the number of ones in the `i`<sup>`th`</sup> row be `onesRow`<sub>`i`</sub>.
- Let the number of ones in the `j`<sup>th</sup> column be `onesCol`<sub>`j`</sub>.
- Let the number of zeros in the `i`<sup>`th`</sup> row be `zerosRow`<sub>`i`</sub>.
- Let the number of zeros in the `j`<sup>`th`</sup> column be `zerosCol`<sub>`j`</sub>.
- `diff[i][j] = onesRow`<sub>`i`</sub>` + onesCol`<sub>`j`</sub>` - zerosRow`<sub>`i`</sub>` - zerosCol`<sub>`j`</sub>

Return the _difference matrix_ `diff`.

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2022/11/06/image-20221106171729-5.png)

Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]
Explanation:

- diff[0][0] = onesRow<sub>0</sub> + onesCol<sub>0</sub> - zerosRow<sub>0</sub> - zerosCol<sub>0</sub> = 2 + 1 - 1 - 2 = 0
- diff[0][1] = onesRow<sub>0</sub> + onesCol<sub>1</sub> - zerosRow<sub>0</sub> - zerosCol<sub>1</sub> = 2 + 1 - 1 - 2 = 0
- diff[0][2] = onesRow<sub>0</sub> + onesCol<sub>2</sub> - zerosRow<sub>0</sub> - zerosCol<sub>2</sub> = 2 + 3 - 1 - 0 = 4
- diff[1][0] = onesRow<sub>1</sub> + onesCol<sub>0</sub> - zerosRow<sub>1</sub> - zerosCol<sub>0</sub> = 2 + 1 - 1 - 2 = 0
- diff[1][1] = onesRow<sub>1</sub> + onesCol<sub>1</sub> - zerosRow<sub>1</sub> - zerosCol<sub>1</sub> = 2 + 1 - 1 - 2 = 0
- diff[1][2] = onesRow<sub>1</sub> + onesCol<sub>2</sub> - zerosRow<sub>1</sub> - zerosCol<sub>2</sub> = 2 + 3 - 1 - 0 = 4
- diff[2][0] = onesRow<sub>2</sub> + onesCol<sub>0</sub> - zerosRow<sub>2</sub> - zerosCol<sub>0</sub> = 1 + 1 - 2 - 2 = -2
- diff[2][1] = onesRow<sub>2</sub> + onesCol<sub>1</sub> - zerosRow<sub>2</sub> - zerosCol<sub>1</sub> = 1 + 1 - 2 - 2 = -2
- diff[2][2] = onesRow<sub>2</sub> + onesCol<sub>2</sub> - zerosRow<sub>2</sub> - zerosCol<sub>2</sub> = 1 + 3 - 2 - 0 = 2

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2022/11/06/image-20221106171747-6.png)

Input: grid = [[1,1,1],[1,1,1]]
Output: [[5,5,5],[5,5,5]]
Explanation:

- diff[0][0] = onesRow<sub>0</sub> + onesCol<sub>0</sub> - zerosRow<sub>0</sub> - zerosCol<sub>0</sub> = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow<sub>0</sub> + onesCol<sub>1</sub> - zerosRow<sub>0</sub> - zerosCol<sub>1</sub> = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow<sub>0</sub> + onesCol<sub>2</sub> - zerosRow<sub>0</sub> - zerosCol<sub>2</sub> = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow<sub>1</sub> + onesCol<sub>0</sub> - zerosRow<sub>1</sub> - zerosCol<sub>0</sub> = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow<sub>1</sub> + onesCol<sub>1</sub> - zerosRow<sub>1</sub> - zerosCol<sub>1</sub> = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow<sub>1</sub> + onesCol<sub>2</sub> - zerosRow<sub>1</sub> - zerosCol<sub>2</sub> = 3 + 2 - 0 - 0 = 5

Constraints:

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`<sup>`5`</sup>
- `1 <= m * n <= 10`<sup>`5`</sup>
- `grid[i][j]` is either `0` or `1`.

## S

### Python

```python
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        # Calc total no of 1s
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                rows[i] += v
                cols[j] += v

        # Diff for each cell using the formula
        diff = [[0] * n for _ in range(m)]
        for i, r in enumerate(rows):
            for j, c in enumerate(cols):
                # r and c are total 1s, so (length - r) or (length - c) are total 0s
                diff[i][j] = r + c - (n - r) - (m - c)
        return diff
```
