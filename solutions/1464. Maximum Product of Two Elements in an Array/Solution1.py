from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i,j = sorted(nums, reverse=True)[:2]
        return (i-1)*(j-1)