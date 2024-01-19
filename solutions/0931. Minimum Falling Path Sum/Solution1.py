from typing import List


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