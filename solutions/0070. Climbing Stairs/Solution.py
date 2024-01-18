class Solution:
    def climbStairs(self, n: int) -> int:
        # DP with Tree DFS, We can use cache, 
        # THEN we move to the solution for Fibonacci
        
        first, second = 1,1

        for i in range(n-1):
            first, second = first+second, first
        return first