from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for r in range(1,n):
            for c in range(n):
                mid = matrix[r-1][c]
                left = matrix[r-1][c-1] if c > 0 else float('inf') # handle left out of bound issue, with bigger number so that it will just be invalid
                right = matrix[r-1][c+1] if c < n - 1 else float('inf') # same for right out of bound

                matrix[r][c] = matrix[r][c] + min(left, mid, right) # assign the sum of curr + min value for optimal solution
        
        return min(matrix[-1]) # last row will have calculations of each previous rows for min value