from collections import Counter
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]
        n = len(nums)
        count = Counter(nums)

        for i in range(1,n+1):
            if count[i] == 0:
                res[1] = i
            if count[i] == 2:
                res[0] = i
        return res
