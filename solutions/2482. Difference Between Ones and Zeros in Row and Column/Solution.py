from typing import List


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