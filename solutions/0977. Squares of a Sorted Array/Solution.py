from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = list(map(lambda x: x**2, nums))
        res.sort()
        return res