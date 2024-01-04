from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for c in count.values():
            if c == 1:
                return -1
            ans += (c + 2) // 3 # math.ciel(c/3)
        return ans