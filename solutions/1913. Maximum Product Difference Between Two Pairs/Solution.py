from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        w,x,y,z = nums[-2:] + nums[:2]
        return (w*x) - (y*z)