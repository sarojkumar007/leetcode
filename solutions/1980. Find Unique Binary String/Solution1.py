from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join("01"[nums[i][i] == '0'] for i in range(len(nums)))