from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        p1 = p2 = 0

        for n in nums:
            temp = max(n+p1,p2)
            p1 = p2
            p2 = temp
        
        return p2