from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hash = Counter(nums)
        res = []
        for item, occurance in hash.items():
            for i in range(occurance):
                if len(res) <= i:
                    res.append([])
                res[i].append(item)
        return res